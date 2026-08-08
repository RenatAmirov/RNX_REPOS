// === Стоп-слова и водные конструкции ===
const STOP_WORDS_RU = new Set([
  // местоимения
  'я', 'мы', 'ты', 'вы', 'он', 'она', 'оно', 'они', 'себя',
  'мой', 'твой', 'свой', 'его', 'её', 'их',
  'кто', 'что', 'какой', 'который', 'чей',
  // междометия и вводные
  'ах', 'ох', 'увы', 'ага', 'ого', 'эй', 'ну', 'вот',
  'конечно', 'вероятно', 'кажется', 'по-моему', 'итак',
  'кстати', 'впрочем', 'однако', 'значит', 'пожалуй',
  // предлоги, союзы, частицы
  'в', 'на', 'с', 'по', 'к', 'от', 'из', 'до', 'для', 'без',
  'и', 'а', 'но', 'или', 'что', 'чтобы', 'как', 'если',
  'не', 'ни', 'бы', 'же', 'ли', 'то', 'это',
  // водные из Главреда
  'следует', 'необходимо', 'важно', 'данный', 'данная',
  'является', 'осуществлять', 'производить', 'обеспечивать'
]);

const STOP_WORDS_EN = new Set([
  'i', 'me', 'my', 'we', 'us', 'our', 'you', 'your',
  'he', 'she', 'it', 'they', 'them', 'their',
  'a', 'an', 'the', 'and', 'or', 'but', 'not', 'no',
  'is', 'are', 'was', 'were', 'be', 'been', 'being',
  'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
  'can', 'could', 'should', 'may', 'might', 'must',
  'this', 'that', 'these', 'those',
  'in', 'on', 'at', 'by', 'for', 'with', 'about', 'to', 'from',
  'actually', 'basically', 'literally', 'really', 'just', 'very',
  'quite', 'rather', 'somehow', 'anyway'
]);

// === Вспомогательные функции ===
function detectLanguage(text) {
  // если есть кириллические символы, считаем русским
  return /[а-яё]/i.test(text) ? 'ru' : 'en';
}

// Токенизация с поддержкой Unicode и апострофов
function tokenize(text) {
  return text.match(/[\w'’-]+/gu) || [];
}

// Удаление стоп-слов и подсчёт частот значимых слов
function getWordFrequencies(tokens, lang) {
  const stopSet = lang === 'ru' ? STOP_WORDS_RU : STOP_WORDS_EN;
  const freq = new Map();
  for (let token of tokens) {
    const lower = token.toLowerCase();
    if (!stopSet.has(lower)) {
      freq.set(lower, (freq.get(lower) || 0) + 1);
    }
  }
  return freq;
}

// === Определение подлежащего и сказуемого ===
// --- Английский (Compromise) ---
function analyzeEnglish(text) {
  // результат: массив объектов {word, isSubject, isPredicate}
  if (typeof nlp === 'undefined') {
    console.warn('Compromise not loaded. English subjects/predicates will be skipped.');
    return [];
  }
  const doc = nlp(text);
  const sentences = doc.sentences().json();
  const results = [];

  sentences.forEach(sent => {
    const words = tokenize(sent.text);
    // Находим подлежащее (Subject) и глагол (Verb) в предложении
    const subjs = doc.match('#Subject').out('array');
    const verbs = doc.verbs().out('array');
    // Простейшее сопоставление: ищем первое слово из subjs/verbs в tokens
    words.forEach(w => {
      const isSubj = subjs.some(s => s.toLowerCase() === w.toLowerCase());
      const isVerb = verbs.some(v => v.toLowerCase() === w.toLowerCase());
      results.push({ word: w, isSubject: isSubj, isPredicate: isVerb });
    });
  });
  return results;
}

// --- Русский (Az) ---
let azMorph = null;
async function initAz() {
  if (typeof Az !== 'undefined' && !azMorph) {
    azMorph = new Az.Morph();
    // Az требует загрузки словаря; предполагаем, что словарь уже загружен в Az.dict
    if (Az.dict) {
      await azMorph.init(Az.dict);
      console.log('Az morphology initialized');
    }
  }
}

function analyzeRussian(text) {
  if (!azMorph) return []; // нет анализа
  // разбиваем на предложения (упрощённо)
  const sentences = text.split(/[.!?]+/).filter(s => s.trim().length > 0);
  const results = [];
  sentences.forEach(sent => {
    const tokens = tokenize(sent);
    const parsed = tokens.map(word => azMorph.parse(word).shift());
    // ищем первое существительное/местоимение в им.падеже как подлежащее
    const subjIdx = parsed.findIndex(p => p && (p.tag.POS === 'NOUN' || p.tag.POS === 'PRON') && p.tag.Case === 'Nom');
    // первое глагольное сказуемое (глагол в личной форме или краткое прилагательное)
    const predIdx = parsed.findIndex(p => p && (p.tag.POS === 'VERB' || p.tag.POS === 'ADJS') && p.tag.VerbForm === 'Fin');
    tokens.forEach((w, i) => {
      results.push({
        word: w,
        isSubject: i === subjIdx,
        isPredicate: i === predIdx
      });
    });
  });
  return results;
}

// === Сборка тултипа ===
async function buildTooltipContent(paragraphText) {
  const lang = detectLanguage(paragraphText);
  const tokens = tokenize(paragraphText);
  const freqMap = getWordFrequencies(tokens, lang);
  const maxFreq = Math.max(1, ...freqMap.values());

  // получаем разметку подлежащего/сказуемого
  let highlights = [];
  if (lang === 'en') {
    highlights = analyzeEnglish(paragraphText);
  } else {
    await initAz();
    highlights = analyzeRussian(paragraphText);
  }

  // создаём HTML-строку
  const words = paragraphText.match(/[\w'’-]+|[^\w'’-]+/gu) || [];
  let html = '';
  words.forEach(segment => {
    if (/[\w'’-]+/u.test(segment)) {
      const lower = segment.toLowerCase();
      const freq = freqMap.get(lower) || 0;
      const scale = freq / maxFreq;           // 0 .. 1
      const fontSize = 14 + Math.round(12 * scale); // 14..26px
      const fontWeight = 400 + Math.round(400 * scale); // 400..800

      // ищем в highlights
      let classes = 'tooltip-word';
      let underlineClass = '';
      if (highlights.length) {
        const h = highlights.find(item => item.word === segment);
        if (h) {
          if (h.isSubject) underlineClass = 'subject';
          if (h.isPredicate) underlineClass = 'predicate';
          classes += ' ' + underlineClass;
        }
      }
      html += `<span class="${classes}" style="font-size:${fontSize}px; font-weight:${fontWeight};">${segment}</span>`;
    } else {
      // знаки препинания, пробелы
      html += segment.replace(/ /g, '&nbsp;');
    }
  });
  return html;
}

// === Управление тултипом ===
let tooltipEl = null;

function createTooltipElement() {
  const div = document.createElement('div');
  div.id = 'paragraph-tooltip';
  div.style.display = 'none';
  document.body.appendChild(div);
  return div;
}

function showTooltip(html, x, y) {
  if (!tooltipEl) tooltipEl = createTooltipElement();
  tooltipEl.innerHTML = html;
  tooltipEl.style.display = 'block';
  tooltipEl.style.left = (x + 15) + 'px';
  tooltipEl.style.top = (y + 15) + 'px';
  // коррекция, чтобы не выходил за границы окна
  const rect = tooltipEl.getBoundingClientRect();
  if (rect.right > window.innerWidth) {
    tooltipEl.style.left = (x - rect.width - 15) + 'px';
  }
  if (rect.bottom > window.innerHeight) {
    tooltipEl.style.top = (y - rect.height - 15) + 'px';
  }
}

function hideTooltip() {
  if (tooltipEl) {
    tooltipEl.style.display = 'none';
  }
}

// === Обработчики событий ===
document.addEventListener('mouseover', async (e) => {
  const p = e.target.closest('p');
  if (!p) return;

  const text = p.textContent.trim();
  if (text.length === 0) return;

  try {
    const html = await buildTooltipContent(text);
    showTooltip(html, e.clientX, e.clientY);
  } catch (err) {
    console.error('Tooltip error:', err);
  }
}, true);

document.addEventListener('mousemove', (e) => {
  if (!tooltipEl || tooltipEl.style.display === 'none') return;
  // двигаем тултип за курсором только если он внутри параграфа
  const p = e.target.closest('p');
  if (p) {
    tooltipEl.style.left = (e.clientX + 15) + 'px';
    tooltipEl.style.top = (e.clientY + 15) + 'px';
  }
});

document.addEventListener('mouseout', (e) => {
  const p = e.target.closest('p');
  if (p && !p.contains(e.relatedTarget)) {
    hideTooltip();
  }
});

// очистка при уходе со страницы
window.addEventListener('beforeunload', () => {
  if (tooltipEl) tooltipEl.remove();
});