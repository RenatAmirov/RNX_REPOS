// ========== 1. Стеммеры ==========

// Русский стеммер (упрощённый Snowball)
function stemRussian(word) {
  word = word.toLowerCase().replace(/ё/g, 'е');
  if (word.length < 3) return word;

  // RV-область: после первой гласной
  const vowel = /[аеиоуыэюя]/;
  let rvStart = word.search(vowel);
  if (rvStart < 0) return word;
  rvStart++;

  // Удаление окончаний
  const perfectiveGerund = /(в|вши|вшись|(ив|ыв|ав|яв)(ши|сь))$/;
  const adjective = /(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$/;
  const participle = /(ем|нн|вш|ющ|щ|ивш|ывш|увш|авш|явш)$/;
  const reflexive = /(ся|сь)$/;
  const verb = /(ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)$/;
  const noun = /(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$/;
  const superlative = /(ейш|ейше)$/;
  const derivational = /(ость|ост)$/;

  // Шаг 1: удалить 'ся'/'сь'
  word = word.replace(reflexive, '');

  // Попытаться отсечь по порядку
  if (word.replace(perfectiveGerund, '').length >= rvStart) {
    word = word.replace(perfectiveGerund, '');
  } else {
    word = word.replace(reflexive, ''); // на случай уже удалённого
    if (word.replace(adjective, '').length >= rvStart) {
      word = word.replace(adjective, '');
      word = word.replace(participle, '');
    } else if (word.replace(verb, '').length >= rvStart) {
      word = word.replace(verb, '');
    } else if (word.replace(noun, '').length >= rvStart) {
      word = word.replace(noun, '');
    }
  }

  // Шаг 2: удалить 'и' в конце основы
  word = word.replace(/и$/, '');

  // Шаг 3: удалить производный суффикс 'ость'/'ост'
  if (word.replace(derivational, '').length >= rvStart) {
    word = word.replace(derivational, '');
  }

  // Шаг 4: удалить 'ь'
  word = word.replace(/ь$/, '');

  return word;
}

// Английский стеммер (Porter)
function stemEnglish(word) {
  word = word.toLowerCase();
  if (word.length < 3) return word;

  // Step 1a
  word = word.replace(/(ss|i)es$/, '$1');
  word = word.replace(/([^s])s$/, '$1');

  // Step 1b
  if (word.match(/(eed)$/)) {
    if (word.slice(0, -3).match(/[aeiou]/)) word = word.slice(0, -1);
  } else if (word.match(/(ed|ing)$/)) {
    let stem = word.replace(/(ed|ing)$/, '');
    if (stem.match(/[aeiou]/)) {
      word = stem;
      if (word.match(/(at|bl|iz)$/)) word += 'e';
      else if (word.match(/([^aeiouylsz])\1$/)) word = word.slice(0, -1);
      else if (word.match(/^[^aeiou]+[aeiou][^aeiouwxy]$/)) word += 'e';
    }
  }

  // Step 1c
  if (word.match(/y$/) && word.slice(0, -1).match(/[aeiou]/)) word = word.slice(0, -1) + 'i';

  // Step 2
  const step2Map = {
    tional: 'tion', enci: 'ence', anci: 'ance', izer: 'ize', abli: 'able',
    alli: 'al', entli: 'ent', eli: 'e', ousli: 'ous', ization: 'ize',
    ation: 'ate', ator: 'ate', alism: 'al', iveness: 'ive', fulness: 'ful',
    ousness: 'ous', aliti: 'al', iviti: 'ive', biliti: 'ble',
  };
  for (let [suf, rep] of Object.entries(step2Map)) {
    if (word.endsWith(suf) && word.slice(0, -suf.length).match(/[aeiou]/)) {
      word = word.slice(0, -suf.length) + rep;
      break;
    }
  }

  // Step 3
  const step3Map = {
    icate: 'ic', ative: '', alize: 'al', iciti: 'ic', ical: 'ic',
    ful: '', ness: '',
  };
  for (let [suf, rep] of Object.entries(step3Map)) {
    if (word.endsWith(suf) && word.slice(0, -suf.length).match(/[aeiou]/)) {
      word = word.slice(0, -suf.length) + rep;
      break;
    }
  }

  // Step 4
  const step4Suffixes = ['al', 'ance', 'ence', 'er', 'ic', 'able', 'ible', 'ant', 'ement', 'ment', 'ent', 'ou', 'ism', 'ate', 'iti', 'ous', 'ive', 'ize'];
  for (let suf of step4Suffixes) {
    if (word.endsWith(suf) && word.slice(0, -suf.length).match(/[aeiou]./)) {
      word = word.slice(0, -suf.length);
      break;
    }
  }

  // Step 5a
  if (word.endsWith('e')) {
    let stem = word.slice(0, -1);
    if (stem.match(/[aeiou]./) || (stem.match(/[aeiou]/) && !stem.match(/[^aeiou][aeiou][^aeiouwxy]$/))) {
      word = stem;
    }
  }
  if (word.endsWith('ll') && word.slice(0, -2).match(/[aeiou]./)) word = word.slice(0, -1);

  return word;
}

// Универсальный стеммер (по языку)
function stem(word, lang) {
  return lang === 'ru' ? stemRussian(word) : stemEnglish(word);
}

// ========== 2. Стоп-слова (водность, местоимения, междометия) ==========
const RU_STOP = new Set([
  'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'но', 'его',
  'по', 'из', 'же', 'у', 'от', 'за', 'для', 'ты', 'мы', 'вы', 'они', 'это', 'ее', 'к', 'до', 'о', 'об',
  'или', 'бы', 'еще', 'уж', 'уже', 'ли', 'только', 'вот', 'там', 'тут', 'где', 'куда', 'откуда', 'когда',
  'почему', 'зачем', 'ну', 'ка', 'ой', 'ах', 'ох', 'эх', 'увы', 'фу', 'ба', 'гм', 'ага', 'ого', 'вау',
  'себя', 'себе', 'собой', 'меня', 'мне', 'мной', 'тебя', 'тебе', 'тобой', 'его', 'ему', 'им', 'нее', 'ней',
  'нами', 'вами', 'ими', 'мой', 'твой', 'свой', 'наш', 'ваш', 'их', 'этот', 'тот', 'такой', 'весь', 'сам',
  'каждый', 'кто', 'чей', 'сколько', 'да', 'нет', 'ни', 'будто', 'словно', 'точно'
]);

const EN_STOP = new Set([
  'i', 'me', 'my', 'mine', 'myself', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
  'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'we', 'us', 'our', 'ours', 'ourselves',
  'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'whose', 'that', 'this',
  'these', 'those', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at',
  'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above',
  'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
  'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both', 'each', 'few', 'more', 'most', 'other',
  'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can',
  'will', 'just', 'don', 'should', 'now', 'oh', 'ah', 'hey', 'wow', 'oops', 'ouch', 'hmm', 'er', 'um', 'uh',
  'alas'
]);

function isStop(lower, lang) {
  return lang === 'ru' ? RU_STOP.has(lower) : EN_STOP.has(lower);
}

function detectLang(word) {
  // Если содержит кириллицу – русский, иначе английский
  return /[а-яё]/i.test(word) ? 'ru' : 'en';
}

// ========== 3. Построение HTML с весами ==========
function buildWeightedHTML(text) {
  const wordRegex = /[\p{L}\u0027\u002D]+/gu;
  const tokens = [];
  let match;
  // Собираем все слова для подсчёта частот
  while ((match = wordRegex.exec(text)) !== null) {
    const original = match[0];
    const lower = original.toLowerCase();
    const lang = detectLang(lower);
    if (!isStop(lower, lang)) {
      tokens.push({ original, lower, lang });
    } else {
      tokens.push({ original, lower, lang, stop: true });
    }
  }

  // Подсчёт частот значимых слов
  const freqMap = new Map();
  for (const t of tokens) {
    if (t.stop) continue;
    const root = stem(t.lower, t.lang);
    freqMap.set(root, (freqMap.get(root) || 0) + 1);
  }

  // Найти диапазон частот
  let minFreq = Infinity, maxFreq = -Infinity;
  for (let count of freqMap.values()) {
    if (count < minFreq) minFreq = count;
    if (count > maxFreq) maxFreq = count;
  }
  if (minFreq === Infinity) minFreq = 0; // нет значимых слов

  const baseSize = 14;
  const maxSize = 32;
  const range = maxFreq - minFreq || 1;

  // Перестройка текста с обёрткой слов в <span>
  let result = '';
  let lastIdx = 0;
  const allMatches = [...text.matchAll(wordRegex)];
  for (const m of allMatches) {
    // Добавляем текст между словами
    result += escapeHTML(text.slice(lastIdx, m.index));
    const original = m[0];
    const lower = original.toLowerCase();
    const lang = detectLang(lower);
    let fontSize = baseSize;
    let fontWeight = 'normal';
    if (!isStop(lower, lang)) {
      const root = stem(lower, lang);
      const freq = freqMap.get(root) || 0;
      const ratio = (freq - minFreq) / range;
      fontSize = baseSize + (maxSize - baseSize) * ratio;
      fontWeight = ratio > 0.6 ? 'bold' : (ratio > 0.3 ? '600' : 'normal');
    }
    result += `<span style="font-size:${fontSize}px;font-weight:${fontWeight}">${escapeHTML(original)}</span>`;
    lastIdx = m.index + original.length;
  }
  result += escapeHTML(text.slice(lastIdx));
  return result;
}

function escapeHTML(str) {
  const div = document.createElement('div');
  div.appendChild(document.createTextNode(str));
  return div.innerHTML;
}

// ========== 4. Всплывающее окно и обработчики ==========
const popup = document.createElement('div');
popup.id = 'word-freq-popup';
popup.style.cssText = `
  position: fixed; background: #fff; border: 1px solid #aaa;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.2); border-radius: 6px;
  padding: 12px 16px; max-width: 600px; max-height: 400px; overflow-y: auto;
  z-index: 999999; pointer-events: auto; line-height: 1.5; font-family: sans-serif;
  display: none;
`;
document.body.appendChild(popup);

let currentPara = null;
let hideTimeout = null;

function showPopup(para, event) {
  if (currentPara === para) return;
  if (currentPara) hidePopup();

  // Кешируем построенный HTML на элементе
  if (!para.dataset.weightedHtml) {
    const text = para.innerText;
    if (!text.trim()) return;
    para.dataset.weightedHtml = buildWeightedHTML(text);
  }
  popup.innerHTML = para.dataset.weightedHtml;
  popup.style.display = 'block';
  positionPopup(event.clientX, event.clientY);
  currentPara = para;
  clearTimeout(hideTimeout);
}

function hidePopup() {
  popup.style.display = 'none';
  currentPara = null;
}

function positionPopup(mx, my) {
  const gap = 15;
  let left = mx + gap;
  let top = my + gap;
  const rect = popup.getBoundingClientRect();
  if (left + rect.width > window.innerWidth) left = mx - rect.width - gap;
  if (top + rect.height > window.innerHeight) top = my - rect.height - gap;
  popup.style.left = Math.max(0, left) + 'px';
  popup.style.top = Math.max(0, top) + 'px';
}

document.addEventListener('mouseover', (e) => {
  const para = e.target.closest('p');
  if (!para) return;
  showPopup(para, e);
});

document.addEventListener('mouseout', (e) => {
  const para = e.target.closest('p');
  if (para && currentPara === para) {
    // Небольшая задержка, чтобы можно было навести на popup
    hideTimeout = setTimeout(() => {
      // Если мышь не над popup, скрыть
      if (!popup.matches(':hover')) hidePopup();
    }, 100);
  }
});

popup.addEventListener('mouseenter', () => clearTimeout(hideTimeout));
popup.addEventListener('mouseleave', () => {
  hideTimeout = setTimeout(hidePopup, 100);
});

// Если ушли с параграфа и не вернулись на popup – скрываем через таймаут
document.addEventListener('mousemove', (e) => {
  if (currentPara && !currentPara.matches(':hover') && !popup.matches(':hover')) {
    hideTimeout = setTimeout(hidePopup, 200);
  }
});