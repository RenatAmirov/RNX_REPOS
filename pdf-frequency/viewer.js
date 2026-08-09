// Настройки PDF.js
pdfjsLib.GlobalWorkerOptions.workerSrc = 'pdfjs/pdf.worker.min.js';

// ------------------- Стеммеры и стоп-слова -------------------
// (полностью копируем из предыдущего ответа, без изменений)

const step2list = {
  ational:"ate", tional:"tion", enci:"ence", anci:"ance", izer:"ize", bli:"ble", alli:"al",
  entli:"ent", eli:"e", ousli:"ous", ization:"ize", ation:"ate", ator:"ate", alism:"al",
  iveness:"ive", fulness:"ful", ousness:"ous", aliti:"al", iviti:"ive", biliti:"ble", logi:"log"
};
const step3list = {
  icate:"ic", ative:"", alize:"al", iciti:"ic", ical:"ic", ful:"", ness:""
};
const c = "[^aeiou]", v = "[aeiouy]",
      C = c + "[^aeiouy]*", V = v + "[aeiou]*",
      mgr0 = "^(" + C + ")?" + V + C,
      meq1 = "^(" + C + ")?" + V + C + "(" + V + ")?$",
      mgr1 = "^(" + C + ")?" + V + C + V + C,
      s_v = "^(" + C + ")?" + v;

function stemEn(w) {
  if (w.length < 3) return w;
  if (w.substr(0,2)==="qu") w = w.substr(2);
  let stem, suffix, fp;
  // 1a
  let re = /^(.+?)(ss|i)es$/, re2 = /^(.+?)([^s])s$/;
  if (re.test(w)) w = w.replace(re,"$1$2");
  else if (re2.test(w)) w = w.replace(re2,"$1$2");
  // 1b
  re = /^(.+?)eed$/; re2 = /^(.+?)(ed|ing)$/;
  if (re.test(w)) {
    fp = re.exec(w);
    if (new RegExp(mgr0).test(fp[1])) w = w.replace(/.$/,"");
  } else if (re2.test(w)) {
    fp = re2.exec(w);
    stem = fp[1];
    if (new RegExp(s_v).test(stem)) {
      w = stem;
      if (/(at|bl|iz)$/.test(w)) w += "e";
      else if (new RegExp("([^aeiouylsz])\\1$").test(w)) w = w.replace(/.$/,"");
      else if (new RegExp("^"+C+v+"[^aeiouwxy]$").test(w)) w += "e";
    }
  }
  // 1c
  re = /^(.+?)y$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(s_v).test(stem)) w = stem + "i";
  }
  // 2
  re = /^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1]; suffix = fp[2];
    if (new RegExp(mgr0).test(stem)) w = stem + step2list[suffix];
  }
  // 3
  re = /^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1]; suffix = fp[2];
    if (new RegExp(mgr0).test(stem)) w = stem + step3list[suffix];
  }
  // 4
  re = /^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$/;
  re2 = /^(.+?)(s|t)(ion)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(mgr1).test(stem)) w = stem;
  } else if (re2.test(w)) {
    fp = re2.exec(w); stem = fp[1] + fp[2];
    if (new RegExp(mgr1).test(stem)) w = stem;
  }
  // 5a
  re = /^(.+?)e$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(mgr1).test(stem) ||
       (new RegExp(meq1).test(stem) && !new RegExp("^"+C+v+"[^aeiouwxy]$").test(stem))) w = stem;
  }
  // 5b
  re = /ll$/;
  if (re.test(w) && new RegExp(mgr1).test(w)) w = w.replace(/l$/,"");
  return w;
}

function stemRu(w) {
  w = w.toLowerCase().replace(/ё/g,"е");
  if (w.length < 3) return w;
  const perfectiveGround = /(ив|ивши|ившись|ыв|ывши|ывшись|в|вши|вшись)$/;
  const reflexive = /(с[яь])$/;
  const adjective = /(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$/;
  const participle = /(ем|нн|вш|ющ|щ|ящ|ивш|ывш|ующ)$/;
  const verb = /(ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|ит|ыт|ены|ить|ыть|ишь|ую|ю)$/;
  const noun = /(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$/;
  const superlative = /(ейш|ейше)$/;
  const derivational = /(ост|ость)$/;
  let stem = w;
  if (stem.length > 4) {
    stem = stem.replace(perfectiveGround,"");
    if (stem === w) stem = stem.replace(reflexive,"");
    if (stem !== w) {
      stem = stem.replace(adjective,"").replace(participle,"");
    } else {
      stem = stem.replace(adjective,"").replace(participle,"");
      if (stem !== w) stem = stem.replace(reflexive,"");
    }
    if (stem !== w) stem = stem.replace(verb,"");
    if (stem !== w) stem = stem.replace(noun,"");
    if (stem !== w) stem = stem.replace(superlative,"");
    if (stem !== w) stem = stem.replace(derivational,"");
  }
  if (stem.endsWith("ь")) stem = stem.slice(0,-1);
  return stem;
}

function isCyrillic(word) {
  return /[а-яё]/i.test(word);
}

function getStem(word) {
  const lower = word.toLowerCase();
  return isCyrillic(lower) ? stemRu(lower) : stemEn(lower);
}

// Стоп-слова
const stopWordsSet = new Set();
const rawRuStop = ["и","в","не","что","он","на","я","с","как","а","то","все","она","так","но","по","из","у","же","за","бы","от","для","мы","до","это","ты","его","к","о","ее","мне","быть","весь","этот","тот","мой","твой","свой","который","где","когда","там","потому","если","каждый","время","рука","слово","дело","сам","другой","наш","ваш","их","себя","ничто","кое","такой","очень","весьма","вдруг","впрочем","всегда","даже","еще","здесь","или","между","перед","под","при","про","со","через","чтобы","без","более","менее","всего","тоже","также","словно","точно","будто","никак","нибудь","ли","раз","сейчас","теперь","уже","опять","только","вон","вот","пусть","пока","хоть","иногда","ведь","либо","кроме","однако","ни","вообще","например","довольно","наконец","наверное","возможно","кажется","кстати","итак","следовательно","по-моему","ах","ох","эх","увы","ой","ого","фу","гм","ну","ага","угу","ай","эге","гей","ба","ура","ц","ау","мяу","гав"];
const rawEnStop = ["i","me","my","myself","we","our","ours","you","your","yours","he","him","his","she","her","hers","it","its","they","them","their","theirs","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","can","will","just","should","now","ah","oh","alas","wow","oops","hey","hurray","yes","yeah","nope","well","hmm","erm","uh","um","ouch","whoa"];
rawRuStop.forEach(w => stopWordsSet.add(stemRu(w.toLowerCase())));
rawEnStop.forEach(w => stopWordsSet.add(stemEn(w.toLowerCase())));

function isStopWord(stem) {
  return stopWordsSet.has(stem);
}

// ------------------- Утилиты -------------------
function escapeHTML(str) {
  return str.replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;");
}

function buildFormattedText(text) {
  const tokenRegex = /[a-zA-Zа-яА-ЯёЁ0-9'’-]+|[^a-zA-Zа-яА-ЯёЁ0-9'’-]+/g;
  const rawTokens = text.match(tokenRegex) || [];
  const tokenStem = [];
  const stemFreq = new Map();

  rawTokens.forEach(t => {
    if (/^[a-zA-Zа-яА-ЯёЁ0-9'’-]+$/.test(t)) {
      const stem = getStem(t);
      tokenStem.push({ token: t, stem });
      if (!isStopWord(stem)) {
        stemFreq.set(stem, (stemFreq.get(stem) || 0) + 1);
      }
    } else {
      tokenStem.push({ token: t, stem: null });
    }
  });

  let minFreq = Infinity, maxFreq = -Infinity;
  stemFreq.forEach(f => { if (f < minFreq) minFreq = f; if (f > maxFreq) maxFreq = f; });
  if (minFreq === Infinity) { minFreq = 1; maxFreq = 1; }

  const minSize = 12, maxSize = 48;
  const minWeight = 400, maxWeight = 900;
  function scale(freq) {
    return maxFreq === minFreq ? 0.5 : (freq - minFreq) / (maxFreq - minFreq);
  }

  let html = "";
  tokenStem.forEach(item => {
    if (item.stem === null) {
      html += escapeHTML(item.token);
    } else {
      const freq = stemFreq.get(item.stem) || 0;
      const s = freq ? scale(freq) : 0;
      const size = freq ? minSize + s * (maxSize - minSize) : minSize;
      const weight = freq ? Math.round(minWeight + s * (maxWeight - minWeight)) : 400;
      html += `<span style="font-size:${size}px;font-weight:${weight};">${escapeHTML(item.token)}</span>`;
    }
  });
  return html;
}

// ------------------- Tooltip -------------------
let tooltip = null;
let pinned = false;
let hideTimer = null;
let selectionTimer = null;

function createTooltip() {
  tooltip = document.createElement('div');
  tooltip.id = '__freq_tooltip__';
  document.body.appendChild(tooltip);
  tooltip.addEventListener('mouseenter', () => clearTimeout(hideTimer));
  tooltip.addEventListener('mouseleave', () => {
    if (!pinned) {
      hideTimer = setTimeout(() => {
        if (!pinned && !tooltip.matches(':hover')) hideTooltip();
      }, 150);
    }
  });
}

function hideTooltip() {
  if (!tooltip) return;
  tooltip.style.display = 'none';
  tooltip.innerHTML = '';
  pinned = false;
  clearTimeout(hideTimer);
  clearTimeout(selectionTimer);
  selectionTimer = null;
}

function positionTooltip(x, y) {
  const rect = tooltip.getBoundingClientRect();
  const vw = window.innerWidth, vh = window.innerHeight;
  let left = x + 12, top = y + 12;
  if (left + rect.width > vw - 8) left = vw - rect.width - 8;
  if (top + rect.height > vh - 8) top = vh - rect.height - 8;
  if (left < 8) left = 8;
  if (top < 8) top = 8;
  tooltip.style.left = left + 'px';
  tooltip.style.top = top + 'px';
}

function showTooltip(text, x, y, pin) {
  if (!tooltip) createTooltip();
  if (pinned && !pin) return;
  clearTimeout(selectionTimer);
  tooltip.innerHTML = buildFormattedText(text);
  tooltip.style.display = 'block';
  pinned = !!pin;
  requestAnimationFrame(() => positionTooltip(x, y));
}

// ------------------- Логика PDF -------------------
const container = document.getElementById('container');
const canvas = document.getElementById('pdf-canvas');
const textLayerDiv = document.getElementById('text-layer');
const ctx = canvas.getContext('2d');

// Получаем URL из параметров
const params = new URLSearchParams(window.location.search);
const fileUrl = params.get('file');
if (!fileUrl) {
  document.body.innerHTML = '<h1 style="color:white;">Не указан PDF-файл</h1>';
  throw new Error('No file');
}

let pdfDoc = null;
let currentPage = 1;
let paragraphs = []; // массив абзацев: {text, bbox: {x,y,w,h}}

// Группируем текстовые блоки в абзацы
function buildParagraphs(textItems) {
  // textItems: [{str, transform: [a,b,c,d,tx,ty], width, height}]
  if (!textItems.length) return [];
  // сортируем по Y, затем X
  const sorted = [...textItems].sort((a, b) => {
    const yA = a.transform[5], yB = b.transform[5];
    if (Math.abs(yA - yB) < 5) return a.transform[4] - b.transform[4];
    return yA - yB;
  });

  const paras = [];
  let currentPara = { text: '', bbox: null, items: [] };

  for (const item of sorted) {
    const x = item.transform[4];
    const y = item.transform[5];
    const w = item.width;
    const h = item.height;
    const prev = currentPara.items[currentPara.items.length - 1];

    if (prev) {
      const prevY = prev.transform[5];
      // новый абзац, если разрыв по вертикали больше высоты строки * 1.5
      if (y - (prevY + prev.height) > prev.height * 1.5) {
        // сохраняем предыдущий абзац
        if (currentPara.text.trim()) {
          const merged = mergeBboxes(currentPara.items);
          paras.push({ text: currentPara.text.trim(), bbox: merged });
        }
        currentPara = { text: '', bbox: null, items: [] };
      }
    }
    currentPara.items.push(item);
    currentPara.text += item.str + (item.hasEOL ? ' ' : '');
  }
  if (currentPara.text.trim()) {
    const merged = mergeBboxes(currentPara.items);
    paras.push({ text: currentPara.text.trim(), bbox: merged });
  }
  return paras;
}

function mergeBboxes(items) {
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  for (const it of items) {
    const x = it.transform[4], y = it.transform[5];
    minX = Math.min(minX, x);
    minY = Math.min(minY, y);
    maxX = Math.max(maxX, x + it.width);
    maxY = Math.max(maxY, y + it.height);
  }
  return { x: minX, y: minY, w: maxX - minX, h: maxY - minY };
}

async function renderPage(num) {
  const page = await pdfDoc.getPage(num);
  const viewport = page.getViewport({ scale: 1.5 });
  canvas.width = viewport.width;
  canvas.height = viewport.height;
  canvas.style.width = viewport.width + 'px';
  canvas.style.height = viewport.height + 'px';

  container.style.width = viewport.width + 'px';
  textLayerDiv.style.width = viewport.width + 'px';
  textLayerDiv.style.height = viewport.height + 'px';

  const renderContext = { canvasContext: ctx, viewport };
  await page.render(renderContext).promise;

  const textContent = await page.getTextContent();
  const items = textContent.items.map(item => ({
    str: item.str,
    transform: item.transform,
    width: item.width,
    height: item.height,
    hasEOL: item.hasEOL || false
  }));

  paragraphs = buildParagraphs(items);

  // Исправленный вызов renderTextLayer
  textLayerDiv.innerHTML = '';
  const textLayerRenderTask = pdfjsLib.renderTextLayer({
    textContent: textContent,   // <-- исправлено
    container: textLayerDiv,
    viewport: viewport
  });
  await textLayerRenderTask.promise;

  setupTextLayerEvents();
}

// События: hover по абзацам и выделение текста
function getParagraphAtPoint(x, y) {
  // координаты относительно страницы
  for (const para of paragraphs) {
    const { bbox } = para;
    if (x >= bbox.x && x <= bbox.x + bbox.w && y >= bbox.y && y <= bbox.y + bbox.h) {
      return para;
    }
  }
  return null;
}

function setupTextLayerEvents() {
  textLayerDiv.onmousemove = function(e) {
    if (pinned) return;
    const rect = textLayerDiv.getBoundingClientRect();
    const scaleX = canvas.width / rect.width;
    const scaleY = canvas.height / rect.height;
    const x = (e.clientX - rect.left) * scaleX;
    const y = (e.clientY - rect.top) * scaleY;
    const para = getParagraphAtPoint(x, y);
    if (para) {
      showTooltip(para.text, e.clientX, e.clientY, false);
      clearTimeout(hideTimer);
    } else {
      clearTimeout(hideTimer);
      hideTimer = setTimeout(() => {
        if (!pinned && !tooltip.matches(':hover')) hideTooltip();
      }, 150);
    }
  };

  textLayerDiv.onmouseleave = function() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(() => {
      if (!pinned && !tooltip.matches(':hover')) hideTooltip();
    }, 150);
  };

  // Выделение мышью
  textLayerDiv.addEventListener('mouseup', function(e) {
    setTimeout(() => {
      const sel = window.getSelection();
      if (!sel.isCollapsed && sel.toString().trim().length > 0) {
        showTooltip(sel.toString(), e.clientX, e.clientY, true);
        pinned = true;
      }
    }, 10);
  });

  // Выделение клавиатурой (с задержкой)
  document.addEventListener('selectionchange', function() {
    if (pinned) return;
    clearTimeout(selectionTimer);
    const sel = window.getSelection();
    if (sel.isCollapsed || !sel.toString().trim()) return;
    selectionTimer = setTimeout(() => {
      const range = sel.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      if (rect.width === 0 && rect.height === 0) return;
      const x = rect.left + rect.width/2;
      const y = rect.top - 10;
      showTooltip(sel.toString(), x, y, true);
      pinned = true;
    }, 400);
  });

  // Закрытие по клику или клавише
  document.addEventListener('click', function() {
    if (pinned) hideTooltip();
  });
  document.addEventListener('keydown', function() {
    if (pinned) hideTooltip();
  });
}

// Инициализация
(async function init() {
  createTooltip();
  const loadingTask = pdfjsLib.getDocument({ url: fileUrl, cMapUrl: 'pdfjs/cmaps/', cMapPacked: true });
  pdfDoc = await loadingTask.promise;
  await renderPage(1);
  // Для простоты показываем только первую страницу. Можно добавить переключение страниц, но это основа.
})();