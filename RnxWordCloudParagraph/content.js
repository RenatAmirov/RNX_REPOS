// Расширенные списки стоп-слов (русский + английский)
const STOP_WORDS = new Set([
  // Русские местоимения
  'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они',
  'меня', 'тебя', 'его', 'её', 'нас', 'вас', 'их',
  'мне', 'тебе', 'ему', 'ей', 'нам', 'вам', 'им',
  'мной', 'тобой', 'им', 'ею', 'нами', 'вами', 'ими',
  'мой', 'твой', 'его', 'её', 'наш', 'ваш', 'их', 'свой',
  'моя', 'твоя', 'его', 'её', 'наша', 'ваша', 'их',
  'моё', 'твоё', 'его', 'её', 'наше', 'ваше', 'их',
  'мои', 'твои', 'его', 'её', 'наши', 'ваши', 'их',
  'себя', 'себе', 'собой',
  'кто', 'что', 'какой', 'который', 'чей', 'сколько',
  'этот', 'эта', 'это', 'эти',
  'тот', 'та', 'те',
  'такой', 'такая', 'такое', 'такие',
  'весь', 'вся', 'всё', 'все',
  'сам', 'самый', 'каждый', 'любой', 'другой', 'иной',
  // Русские междометия и частицы
  'ах', 'ох', 'ух', 'эх', 'ой', 'ай', 'эй', 'увы', 'фу', 'тьфу',
  'брр', 'цыц', 'брысь', 'прочь', 'ого', 'эге', 'гм', 'хм',
  'ну', 'ведь', 'же', 'ли', 'бы', 'де', 'мол', 'вот', 'вон',
  'да', 'нет', 'лишь', 'только', 'даже', 'именно', 'почти',
  'уже', 'ещё', 'всё', 'раз', 'так', 'тоже', 'также',
  // Водные конструкции и союзы (рус.)
  'и', 'в', 'на', 'с', 'по', 'из', 'от', 'до', 'к', 'за',
  'над', 'под', 'перед', 'о', 'об', 'про', 'у', 'без', 'для',
  'при', 'через', 'около', 'возле', 'между', 'ради',
  'из-за', 'из-под', 'а', 'но', 'или', 'либо', 'то',
  'что', 'чтобы', 'как', 'когда', 'если', 'хотя',
  'потому', 'поэтому', 'так', 'тоже', 'также',
  'не', 'ни',
  // Английские местоимения
  'i', 'you', 'he', 'she', 'it', 'we', 'they',
  'me', 'him', 'her', 'us', 'them',
  'my', 'your', 'his', 'its', 'our', 'their',
  'mine', 'yours', 'hers', 'ours', 'theirs',
  'myself', 'yourself', 'himself', 'herself', 'itself',
  'ourselves', 'yourselves', 'themselves',
  'this', 'that', 'these', 'those',
  'who', 'whom', 'what', 'which', 'whose',
  // Английские междометия
  'oh', 'ah', 'wow', 'ouch', 'hey', 'alas', 'bravo', 'ugh',
  'oops', 'hmm', 'yay', 'phew', 'duh', 'eek', 'huh',
  // Водные слова, союзы, предлоги (англ.)
  'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at',
  'to', 'for', 'of', 'with', 'by', 'from', 'up', 'about',
  'into', 'through', 'during', 'before', 'after', 'above',
  'below', 'between', 'out', 'off', 'over', 'under', 'again',
  'further', 'then', 'once', 'here', 'there', 'when', 'where',
  'why', 'how', 'all', 'both', 'each', 'few', 'more', 'most',
  'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
  'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just',
  'don', 'should', 'now', 'is', 'am', 'are', 'was', 'were',
  'be', 'been', 'being', 'have', 'has', 'had', 'having',
  'do', 'does', 'did', 'doing', 'would', 'could', 'may',
  'might', 'shall', 'must', 'also'
]);

function isStopWord(word) {
  return STOP_WORDS.has(word.toLowerCase());
}

// Разбивает текст на токены: слова и разделители
function tokenize(text) {
  const regex = /([a-zA-Zа-яёЁА-Я0-9]+)|([^a-zA-Zа-яёЁА-Я0-9]+)/g;
  const tokens = [];
  let match;
  while ((match = regex.exec(text)) !== null) {
    if (match[1] !== undefined) {
      tokens.push({ type: 'word', value: match[1], clean: match[1].toLowerCase() });
    } else {
      tokens.push({ type: 'separator', value: match[2] });
    }
  }
  return tokens;
}

// Строит карту частота для значимых слов
function buildFrequencyMap(tokens) {
  const freq = new Map();
  for (const tok of tokens) {
    if (tok.type === 'word' && !isStopWord(tok.clean)) {
      freq.set(tok.clean, (freq.get(tok.clean) || 0) + 1);
    }
  }
  return freq;
}

// Создаёт HTML-строку для всплывающего окна
function buildTooltipHTML(tokens, freqMap) {
  const maxFreq = Math.max(1, ...freqMap.values());
  const minFontSize = 20;
  const maxFontSize = 36;

  let html = '';
  for (const tok of tokens) {
    if (tok.type === 'separator') {
      // Экранируем спецсимволы HTML в разделителях
      const escaped = tok.value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      html += escaped;
    } else {
      const freq = freqMap.get(tok.clean) || 0;
      const original = tok.value.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      if (freq > 0 && maxFreq > 0) {
        const ratio = (freq - 1) / (maxFreq - 1);
        const fontSize = minFontSize + ratio * (maxFontSize - minFontSize);
        const fontWeight = 300 + Math.round(ratio * 400); // от 400 до 900
        html += `<span style="font-size:${fontSize}px;font-weight:${fontWeight};">${original}</span>`;
      } else {
        // стоп-слово или слово без учёта
        html += `<span style="font-size:${minFontSize}px;">${original}</span>`;
      }
    }
  }
  return html;
}

// --- Всплывающее окно ---
let tooltip = null;
let currentP = null;

function createTooltip() {
  const div = document.createElement('div');
  div.id = 'word-freq-tooltip';
  div.style.cssText = `
    position: fixed;
    background: #fff;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    padding: 10px 14px;
    max-width: 500px;
    word-wrap: break-word;
    z-index: 2147483647;
    pointer-events: none;
    line-height: 1.5;
    font-family: Arial, sans-serif;
    display: none;
  `;
  document.body.appendChild(div);
  return div;
}

function showTooltip(e, pElement) {
  if (!tooltip) tooltip = createTooltip();
  const text = pElement.textContent;
  const tokens = tokenize(text);
  const freqMap = buildFrequencyMap(tokens);
  tooltip.innerHTML = buildTooltipHTML(tokens, freqMap);
  tooltip.style.display = 'block';
  updateTooltipPosition(e);
}

function updateTooltipPosition(e) {
  if (!tooltip || tooltip.style.display === 'none') return;
  const offsetX = 15;
  const offsetY = 15;
  let x = e.clientX + offsetX;
  let y = e.clientY + offsetY;
  // Не выходить за пределы окна
  const tooltipRect = tooltip.getBoundingClientRect();
  if (x + tooltipRect.width > window.innerWidth) {
    x = e.clientX - tooltipRect.width - offsetX;
  }
  if (y + tooltipRect.height > window.innerHeight) {
    y = e.clientY - tooltipRect.height - offsetY;
  }
  tooltip.style.left = x + 'px';
  tooltip.style.top = y + 'px';
}

function hideTooltip() {
  if (tooltip) {
    tooltip.style.display = 'none';
    tooltip.innerHTML = '';
  }
  currentP = null;
}

// Обработчики событий
document.addEventListener('mouseover', (e) => {
  const target = e.target.closest('p');
  if (!target) return;
  if (currentP === target) return; // уже показываем
  hideTooltip();
  currentP = target;
  showTooltip(e, target);
});

document.addEventListener('mouseout', (e) => {
  const target = e.target.closest('p');
  if (!target) return;
  if (target === currentP && !target.contains(e.relatedTarget)) {
    hideTooltip();
  }
});

document.addEventListener('mousemove', (e) => {
  if (currentP && tooltip && tooltip.style.display === 'block') {
    updateTooltipPosition(e);
  }
});