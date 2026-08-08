// Списки стоп-слов для русского и английского языков
// (водность: местоимения, предлоги, союзы, частицы, междометия)
const STOP_WORDS = new Set([
  // Русские
  'и', 'в', 'не', 'на', 'я', 'что', 'с', 'он', 'а', 'как', 'это', 'то',
  'все', 'она', 'так', 'но', 'по', 'ты', 'мы', 'вы', 'они', 'к', 'у',
  'из', 'от', 'до', 'о', 'об', 'за', 'над', 'под', 'при', 'про', 'без',
  'для', 'ради', 'через', 'между', 'перед', 'вокруг', 'после', 'против',
  'кроме', 'среди', 'вдоль', 'мимо', 'около', 'благодаря', 'вследствие',
  'ввиду', 'вопреки', 'со', 'во', 'ко', 'обо', 'подо', 'надо', 'предо',
  'меня', 'тебя', 'его', 'её', 'нас', 'вас', 'их', 'мне', 'тебе', 'ему',
  'ей', 'нам', 'вам', 'им', 'мной', 'тобой', 'им', 'ею', 'нами', 'вами',
  'ими', 'мой', 'твой', 'свой', 'наш', 'ваш', 'этот', 'тот', 'такой',
  'весь', 'всякий', 'каждый', 'сам', 'самый', 'кто', 'что', 'какой',
  'чей', 'сколько', 'который', 'или', 'либо', 'то', 'ни', 'тоже', 'также',
  'зато', 'однако', 'потому', 'что', 'чтобы', 'если', 'раз', 'хотя', 'пока',
  'лишь', 'только', 'будто', 'словно', 'точно', 'чем', 'нежели', 'ли', 'же',
  'бы', 'ведь', 'вот', 'вон', 'даже', 'именно', 'почти', 'приблизительно',
  'как', 'раз', 'ах', 'ох', 'эх', 'ух', 'ай', 'ой', 'эй', 'фу', 'фи', 'увы',
  'ага', 'ого', 'ура', 'ба', 'ну', 'брр', 'тьфу', 'бы', 'же', 'да', 'нет',
  // Английские
  'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
  'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
  'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
  'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that',
  'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
  'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
  'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of',
  'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through',
  'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down',
  'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
  'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both', 'each', 'few',
  'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own',
  'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don',
  'should', 'now', 'don\'t', 'doesn\'t', 'isn\'t', 'aren\'t', 'wasn\'t',
  'weren\'t', 'haven\'t', 'hasn\'t', 'hadn\'t', 'won\'t', 'wouldn\'t',
  'shouldn\'t', 'can\'t', 'couldn\'t', 'mightn\'t', 'mustn\'t', 'it\'s',
  'that\'s', 'there\'s', 'here\'s', 'what\'s', 'who\'s', 'let\'s'
]);

// Всплывающий элемент (один на страницу)
let popup = null;

// Предварительный подсчёт частот всех слов на странице при загрузке
const wordFreq = new Map();
let maxFreq = 0;

function tokenize(text) {
  // Разбиваем на слова с учётом русского и английского, включая апострофы
  return text.toLowerCase().match(/[a-zа-яё'’-]+/g) || [];
}

function buildFrequencyMap() {
  const pageText = document.body.innerText || '';
  const tokens = tokenize(pageText);
  for (const token of tokens) {
    if (!STOP_WORDS.has(token)) {
      const count = (wordFreq.get(token) || 0) + 1;
      wordFreq.set(token, count);
      if (count > maxFreq) maxFreq = count;
    }
  }
}

// Создаём единый popup‑контейнер
function createPopup() {
  popup = document.createElement('div');
  popup.id = 'word-freq-popup';
  popup.style.cssText = `
    position: fixed;
    display: none;
    background: white;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    padding: 12px 16px;
    max-width: 600px;
    max-height: 400px;
    overflow-y: auto;
    z-index: 2147483647;
    font-family: Arial, sans-serif;
    line-height: 1.6;
    pointer-events: auto;
  `;
  document.body.appendChild(popup);
}

// Генерируем содержимое попапа для конкретного абзаца
function renderParagraph(paragraphElement) {
  const rawText = paragraphElement.innerText || paragraphElement.textContent || '';
  // Разбиваем с сохранением пробелов и знаков препинания
  const segments = rawText.match(/\S+\s*/g) || [rawText];
  let html = '';
  for (const seg of segments) {
    // Извлекаем «чистое» слово без окружающей пунктуации
    const cleanMatch = seg.match(/[a-zа-яё'’-]+/i);
    if (!cleanMatch) {
      html += seg; // оставляем как есть (например, знаки препинания)
      continue;
    }
    const cleanWord = cleanMatch[0].toLowerCase();
    // Определяем стиль слова
    let fontSize = 14;   // базовый размер для стоп-слов
    let fontWeight = 400;
    if (!STOP_WORDS.has(cleanWord) && wordFreq.has(cleanWord)) {
      const freq = wordFreq.get(cleanWord);
      const ratio = maxFreq > 0 ? freq / maxFreq : 0;
      fontSize = 14 + Math.round(28 * ratio);  // диапазон 14–42px
      fontWeight = 400 + Math.round(300 * ratio); // 400–700
    }
    // Заменяем только слово, сохраняя остальные символы
    const styledToken = seg.replace(cleanMatch[0], `<span style="font-size:${fontSize}px;font-weight:${fontWeight};">${cleanMatch[0]}</span>`);
    html += styledToken;
  }
  popup.innerHTML = html;
}

// Обработчики мыши
function onMouseEnter(e) {
  const p = e.target.closest('p');
  if (!p) return;
  renderParagraph(p);
  positionPopup(e);
  popup.style.display = 'block';
}

function onMouseLeave(e) {
  const p = e.target.closest('p');
  if (!p) return;
  // Проверяем, что мышь действительно покинула абзац, а не перешла на потомка
  if (!p.contains(e.relatedTarget)) {
    popup.style.display = 'none';
  }
}

function positionPopup(e) {
  const x = e.clientX + 15;
  const y = e.clientY + 15;
  popup.style.left = Math.min(x, window.innerWidth - 620) + 'px';
  popup.style.top = Math.min(y, window.innerHeight - 420) + 'px';
}

// Инициализация
function init() {
  buildFrequencyMap();
  createPopup();
  document.addEventListener('mouseover', onMouseEnter, true);
  document.addEventListener('mouseout', onMouseLeave, true);
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}