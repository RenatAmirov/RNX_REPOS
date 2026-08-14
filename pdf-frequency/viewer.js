// Настройки PDF.js
pdfjsLib.GlobalWorkerOptions.workerSrc = 'pdfjs/pdf.worker.min.js';

// ------------------- Стеммеры и стоп-слова -------------------
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
  let re = /^(.+?)(ss|i)es$/, re2 = /^(.+?)([^s])s$/;
  if (re.test(w)) w = w.replace(re,"$1$2");
  else if (re2.test(w)) w = w.replace(re2,"$1$2");
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
  re = /^(.+?)y$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(s_v).test(stem)) w = stem + "i";
  }
  re = /^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1]; suffix = fp[2];
    if (new RegExp(mgr0).test(stem)) w = stem + step2list[suffix];
  }
  re = /^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1]; suffix = fp[2];
    if (new RegExp(mgr0).test(stem)) w = stem + step3list[suffix];
  }
  re = /^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$/;
  re2 = /^(.+?)(s|t)(ion)$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(mgr1).test(stem)) w = stem;
  } else if (re2.test(w)) {
    fp = re2.exec(w); stem = fp[1] + fp[2];
    if (new RegExp(mgr1).test(stem)) w = stem;
  }
  re = /^(.+?)e$/;
  if (re.test(w)) {
    fp = re.exec(w); stem = fp[1];
    if (new RegExp(mgr1).test(stem) ||
       (new RegExp(meq1).test(stem) && !new RegExp("^"+C+v+"[^aeiouwxy]$").test(stem))) w = stem;
  }
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

const stopWordsSet = new Set();
const rawRuStop = ["и","в","не","что","он","на","я","с","как","а","то","все","она","так","но","по","из","у","же","за","бы","от","для","мы","до","это","ты","его","к","о","ее","мне","быть","весь","этот","тот","мой","твой","свой","который","где","когда","там","потому","если","каждый","время","рука","слово","дело","сам","другой","наш","ваш","их","себя","ничто","кое","такой","очень","весьма","вдруг","впрочем","всегда","даже","еще","здесь","или","между","перед","под","при","про","со","через","чтобы","без","более","менее","всего","тоже","также","словно","точно","будто","никак","нибудь","ли","раз","сейчас","теперь","уже","опять","только","вон","вот","пусть","пока","хоть","иногда","ведь","либо","кроме","однако","ни","вообще","например","довольно","наконец","наверное","возможно","кажется","кстати","итак","следовательно","по-моему","ах","ох","эх","увы","ой","ого","фу","гм","ну","ага","угу","ай","эге","гей","ба","ура","ц","ау","мяу","гав"];
const rawEnStop = ["i","me","my","myself","we","our","ours","you","your","yours","he","him","his","she","her","hers","it","its","they","them","their","theirs","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","can","will","just","should","now","ah","oh","alas","wow","oops","hey","hurray","yes","yeah","nope","well","hmm","erm","uh","um","ouch","whoa"];
rawRuStop.forEach(w => stopWordsSet.add(stemRu(w.toLowerCase())));
rawEnStop.forEach(w => stopWordsSet.add(stemEn(w.toLowerCase())));

function isStopWord(stem) {
  return stopWordsSet.has(stem);
}

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
  const vw = window.innerWidth;
  const vh = window.innerHeight;
  const toolbarHeight = document.getElementById('toolbar').getBoundingClientRect().height;

  let left = x + 12;
  let top = y + 12;

  if (left + rect.width > vw - 8) left = vw - rect.width - 8;
  if (top + rect.height > vh - 8) top = vh - rect.height - 8;
  if (left < 8) left = 8;
  if (top < toolbarHeight + 8) top = toolbarHeight + 8;

  tooltip.style.left = left + 'px';
  tooltip.style.top = top + 'px';
}

function showTooltip(text, x, y, pin) {
  if (!tooltip) createTooltip();
  if (pinned && !pin) return;
  clearTimeout(selectionTimer);

  // Размер tooltip – как PDF-контейнер, но не больше экрана (с учётом панели инструментов)
  const containerRect = document.getElementById('container').getBoundingClientRect();
  const toolbarHeight = document.getElementById('toolbar').getBoundingClientRect().height;
  const maxWidth = Math.min(containerRect.width, window.innerWidth - 40);
  const maxHeight = Math.min(containerRect.height, window.innerHeight - toolbarHeight - 40);

  tooltip.style.maxWidth = maxWidth + 'px';
  tooltip.style.maxHeight = maxHeight + 'px';
  // width/height оставляем auto, чтобы контент мог быть меньше

  tooltip.innerHTML = buildFormattedText(text);
  tooltip.style.display = 'block';
  pinned = !!pin;
  requestAnimationFrame(() => positionTooltip(x, y));
}

// ------------------- Навигация и рендеринг -------------------
const container = document.getElementById('container');
const canvas = document.getElementById('pdf-canvas');
const textLayerDiv = document.getElementById('text-layer');
const ctx = canvas.getContext('2d');

const pageNumInput = document.getElementById('page-num');
const totalPagesSpan = document.getElementById('total-pages');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');

const params = new URLSearchParams(window.location.search);
const fileUrl = params.get('file');
if (!fileUrl) {
  document.body.innerHTML = '<h1 style="color:white;">Не указан PDF-файл</h1>';
  throw new Error('No file');
}

let pdfDoc = null;
let currentPage = 1;
let spanToParagraph = new Map();

function buildParagraphsFromSpans() {
  spanToParagraph.clear();
  const spans = textLayerDiv.querySelectorAll('span');
  if (spans.length === 0) return;

  // Группируем span'ы в строки
  const rows = [];
  let currentRow = [];
  let lastY = null;
  const Y_THRESHOLD = 5;

  for (const span of spans) {
    const rect = span.getBoundingClientRect();
    if (rect.width === 0 || rect.height === 0) continue;
    const y = rect.top;
    if (lastY === null || Math.abs(y - lastY) <= Y_THRESHOLD) {
      currentRow.push(span);
    } else {
      if (currentRow.length > 0) rows.push(currentRow);
      currentRow = [span];
    }
    lastY = y;
  }
  if (currentRow.length > 0) rows.push(currentRow);

  // Группируем строки в абзацы
  const paragraphs = [];
  let currentPara = [];
  let lastRowBottom = null;
  const LINE_GAP_THRESHOLD = 10;

  for (const row of rows) {
    const firstSpan = row[0];
    const rowTop = firstSpan.getBoundingClientRect().top;
    if (lastRowBottom !== null) {
      const gap = rowTop - lastRowBottom;
      if (gap > LINE_GAP_THRESHOLD) {
        if (currentPara.length > 0) paragraphs.push(currentPara);
        currentPara = [];
      }
    }
    currentPara.push(row);
    let maxBottom = 0;
    for (const sp of row) {
      const b = sp.getBoundingClientRect().bottom;
      if (b > maxBottom) maxBottom = b;
    }
    lastRowBottom = maxBottom;
  }
  if (currentPara.length > 0) paragraphs.push(currentPara);

  // Привязываем каждый span к тексту его абзаца
  for (const para of paragraphs) {
    const spansInPara = [];
    for (const row of para) {
      row.sort((a, b) => {
        const aRect = a.getBoundingClientRect();
        const bRect = b.getBoundingClientRect();
        return aRect.left - bRect.left;
      });
      spansInPara.push(...row);
    }
    let paraText = '';
    for (const span of spansInPara) {
      paraText += span.textContent + ' ';
    }
    paraText = paraText.replace(/\s+/g, ' ').trim();
    for (const span of spansInPara) {
      spanToParagraph.set(span, paraText);
    }
  }
}

async function renderPage(num) {
  if (!pdfDoc || num < 1 || num > pdfDoc.numPages) return;
  currentPage = num;
  pageNumInput.value = num;

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

  textLayerDiv.innerHTML = '';
  const textLayerRenderTask = pdfjsLib.renderTextLayer({
    textContent: textContent,
    container: textLayerDiv,
    viewport: viewport
  });
  await textLayerRenderTask.promise;

  buildParagraphsFromSpans();
  setupTextLayerEvents();
}

function setupTextLayerEvents() {
  textLayerDiv.onmousemove = function(e) {
    if (pinned) return;
    let target = e.target;
    while (target && target !== textLayerDiv) {
      if (target.tagName === 'SPAN') {
        const text = spanToParagraph.get(target);
        if (text) {
          showTooltip(text, e.clientX, e.clientY, false);
          clearTimeout(hideTimer);
          return;
        }
      }
      target = target.parentElement;
    }
    clearTimeout(hideTimer);
    hideTimer = setTimeout(() => {
      if (!pinned && !tooltip.matches(':hover')) hideTooltip();
    }, 150);
  };

  textLayerDiv.onmouseleave = function() {
    clearTimeout(hideTimer);
    hideTimer = setTimeout(() => {
      if (!pinned && !tooltip.matches(':hover')) hideTooltip();
    }, 150);
  };

  textLayerDiv.addEventListener('mouseup', function(e) {
    setTimeout(() => {
      const sel = window.getSelection();
      if (!sel.isCollapsed && sel.toString().trim().length > 0) {
        showTooltip(sel.toString(), e.clientX, e.clientY, true);
        pinned = true;
      }
    }, 10);
  });

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
  totalPagesSpan.textContent = pdfDoc.numPages;
  pageNumInput.max = pdfDoc.numPages;

  await renderPage(1);

  prevBtn.addEventListener('click', async () => {
    if (currentPage <= 1) return;
    await renderPage(currentPage - 1);
  });
  nextBtn.addEventListener('click', async () => {
    if (currentPage >= pdfDoc.numPages) return;
    await renderPage(currentPage + 1);
  });
  pageNumInput.addEventListener('change', async () => {
    let page = parseInt(pageNumInput.value, 10);
    if (isNaN(page) || page < 1) page = 1;
    if (page > pdfDoc.numPages) page = pdfDoc.numPages;
    if (page !== currentPage) await renderPage(page);
  });
})();