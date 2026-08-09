(function () {
  'use strict';

  // ======================== СТЕММЕРЫ ========================

  // Porter stemmer for English (public domain)
  function porterStemmer(w) {
    if (w.length < 3) return w;
    let step2list = {
      ational: 'ate', tional: 'tion', enci: 'ence', anci: 'ance', izer: 'ize',
      bli: 'ble', alli: 'al', entli: 'ent', eli: 'e', ousli: 'ous',
      ization: 'ize', ation: 'ate', ator: 'ate', alism: 'al',
      iveness: 'ive', fulness: 'ful', ousness: 'ous', aliti: 'al',
      iviti: 'ive', biliti: 'ble', logi: 'log'
    };
    let step3list = {
      icate: 'ic', ative: '', alize: 'al', iciti: 'ic', ical: 'ic', ful: '', ness: ''
    };
    let c = '[^aeiou]', v = '[aeiouy]', C = c + '[^aeiouy]*', V = v + '[aeiou]*';
    let mgr0 = '^(' + C + ')?' + V + C;
    let meq1 = '^(' + C + ')?' + V + C + '(' + V + ')?$';
    let mgr1 = '^(' + C + ')?' + V + C + V + C;
    let sV = '^(' + C + ')?' + v;

    function stem(word) {
      let stem = word.toLowerCase(), fp, re, re2, re3, re4, orig = word;
      if (stem.length < 3) return stem;
      if (stem == 'sky') return stem;
      if (/^[^aeiou]+$/.test(stem[0]) && stem[0] == 'y') stem = 'Y' + stem.substr(1);
      re = /^([^aeiou][^aeiouy]*)?[aeiouy]([^aeiou][^aeiouy]*)?$/;
      if (re.test(stem)) { let fp = stem.match(re); stem = fp[1] + fp[2]; }
      if (/^[^aeiou][^aeiouy]*[aeiouy]/.test(stem) && /[^aeiou][^aeiouy]*$/.test(stem)) {
        re = /^([^aeiou][^aeiouy]*[aeiouy])(.*)/; let m = stem.match(re); stem = m[1] + m[2];
      }
      re = /^(.+?)(ss|i)es$/; re2 = /^(.+?)([^s])s$/;
      if (re.test(stem)) stem = stem.replace(re, '$1$2');
      else if (re2.test(stem)) stem = stem.replace(re2, '$1$2');
      re = /^(.+?)eed$/; re2 = /^(.+?)(ed|ing)$/;
      if (re.test(stem)) { let fp = stem.match(re); re = new RegExp(mgr0); if (re.test(fp[1])) { re = /.$/; stem = stem.replace(re, ''); } }
      else if (re2.test(stem)) {
        let fp = stem.match(re2);
        let s = fp[1];
        re = new RegExp(sV);
        if (re.test(s)) {
          stem = s;
          re = /(at|bl|iz)$/; re2 = new RegExp('([^aeiouylsz])\\1$'); re3 = new RegExp('^' + C + v + '[^aeiouwxy]$');
          if (re.test(stem)) stem = stem + 'e';
          else if (re2.test(stem)) { re = /.$/; stem = stem.replace(re, ''); }
          else if (re3.test(stem)) stem = stem + 'e';
        }
      }
      re = /^(.+?)y$/;
      if (re.test(stem)) { let fp = stem.match(re); let s = fp[1]; re = new RegExp(sV); if (re.test(s)) stem = s + 'i'; }
      re = /^(.+?)(ational|tional|enci|anci|izer|bli|alli|entli|eli|ousli|ization|ation|ator|alism|iveness|fulness|ousness|aliti|iviti|biliti|logi)$/;
      if (re.test(stem)) { let fp = stem.match(re); let s = fp[1]; let suf = fp[2]; re = new RegExp(mgr0); if (re.test(s)) stem = s + step2list[suf]; }
      re = /^(.+?)(icate|ative|alize|iciti|ical|ful|ness)$/;
      if (re.test(stem)) { let fp = stem.match(re); let s = fp[1]; let suf = fp[2]; re = new RegExp(mgr0); if (re.test(s)) stem = s + step3list[suf]; }
      re = /^(.+?)(al|ance|ence|er|ic|able|ible|ant|ement|ment|ent|ou|ism|ate|iti|ous|ive|ize)$/;
      re2 = /^(.+?)(s|t)(ion)$/;
      if (re.test(stem)) { let fp = stem.match(re); let s = fp[1]; re = new RegExp(mgr1); if (re.test(s)) stem = s; }
      else if (re2.test(stem)) { let fp = stem.match(re2); let s = fp[1] + fp[2]; re = new RegExp(mgr1); if (re.test(s)) stem = s; }
      re = /^(.+?)e$/;
      if (re.test(stem)) { let fp = stem.match(re); let s = fp[1]; re = new RegExp(mgr1); re2 = new RegExp(meq1); re3 = new RegExp('^' + C + v + '[^aeiouwxy]$');
        if (re.test(s) || (re2.test(s) && !re3.test(s))) stem = s; }
      re = /ll$/; re2 = new RegExp(mgr1);
      if (re.test(stem) && re2.test(stem)) { re = /.$/; stem = stem.replace(re, ''); }
      if (stem == 'y') stem = 'Y';
      while (stem.length > 0 && stem[0] == 'Y') stem = 'y' + stem.substr(1);
      return stem;
    }
    return stem(w);
  }

  // Simplified Snowball stemmer for Russian (based on public algorithm)
  function russianStemmer(word) {
    word = word.toLowerCase();
    if (word.length < 3) return word;
    const VOWEL = /[аеиоуыэюяё]/;
    const PERFECTIVEGROUND = /(ив|ивши|ившись|ыв|ывши|ывшись)$/;
    const REFLEXIVE = /(с[яь])$/;
    const ADJECTIVE = /(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$/;
    const PARTICIPLE = /(ивш|ывш|ующ|ем|нн|вш|ющ|щ)$/;
    const VERB = /(ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю|ла|на|ете|йте|ли|й|л|ем|н|ло|ет|ют|ны|ть|ешь|нно)$/;
    const NOUN = /(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$/;
    const SUPERLATIVE = /(ейше|ейш)$/;
    const DERIVATIONAL = /(ость|ост)$/;
    const TIDY = /(нн)$/;
    const I = /и$/;
    const P = /ь$/;
    const NN = /нн$/;

    function RV(word) {
      let i = 0;
      while (i < word.length && !VOWEL.test(word[i])) i++;
      i++;
      return word.substring(i);
    }

    function R2(word) {
      let rv = RV(word);
      if (rv.length === 0) return '';
      let i = 0;
      while (i < rv.length && !VOWEL.test(rv[i])) i++;
      i++;
      return rv.substring(i);
    }

    let stem = word;
    let rv = RV(stem);
    if (rv === '') return stem;

    // Step 1: perfective gerund
    let match = rv.match(PERFECTIVEGROUND);
    if (match) {
      stem = stem.substring(0, stem.length - match[0].length);
      rv = RV(stem);
    } else {
      // reflexive
      match = rv.match(REFLEXIVE);
      if (match) {
        stem = stem.substring(0, stem.length - match[0].length);
        rv = RV(stem);
      }
    }

    // Step 2: adjective, participle, verb, noun, superlative
    let found = false;
    if (rv.length > 0) {
      match = rv.match(ADJECTIVE);
      if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); found = true; }
      else {
        match = rv.match(PARTICIPLE);
        if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); found = true; }
        else {
          match = rv.match(VERB);
          if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); found = true; }
          else {
            match = rv.match(NOUN);
            if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); found = true; }
          }
        }
      }
    }

    if (found) {
      match = rv.match(SUPERLATIVE);
      if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); }
    }

    // Step 3: derivational endings
    if (found || (rv.length && rv.match(DERIVATIONAL))) {
      match = rv.match(DERIVATIONAL);
      if (match) { stem = stem.substring(0, stem.length - match[0].length); rv = RV(stem); }
    }

    // Step 4: tidy up
    if (rv.match(TIDY)) {
      stem = stem.replace(NN, 'н');
    } else if (found) {
      if (rv.match(I)) {
        stem = stem.substring(0, stem.length - 1);
        rv = RV(stem);
      }
      if (rv.match(P)) {
        stem = stem.substring(0, stem.length - 1);
      }
    }

    return stem;
  }

  // Определение языка и стемминг
  function stemWord(word) {
    if (/[а-яё]/i.test(word)) {
      return russianStemmer(word);
    } else {
      return porterStemmer(word);
    }
  }

  // ======================== СТОП-СЛОВА ========================

  const stopWordsEn = new Set([
    'a','about','above','after','again','against','all','am','an','and','any','are','aren\'t','as','at',
    'be','because','been','before','being','below','between','both','but','by',
    'can','can\'t','cannot','could','couldn\'t',
    'd','did','didn\'t','do','does','doesn\'t','doing','don\'t','down','during',
    'each','few','for','from','further',
    'had','hadn\'t','has','hasn\'t','have','haven\'t','having','he','he\'d','he\'ll','he\'s','her','here','here\'s','hers','herself','him','himself','his','how','how\'s',
    'i','i\'d','i\'ll','i\'m','i\'ve','if','in','into','is','isn\'t','it','it\'s','its','itself',
    'let\'s',
    'me','more','most','mustn\'t','my','myself',
    'no','nor','not','now',
    'o','of','off','on','once','only','or','other','ought','our','ours','ourselves','out','over','own',
    'same','shan\'t','she','she\'d','she\'ll','she\'s','should','shouldn\'t','so','some','such',
    'than','that','that\'s','the','their','theirs','them','themselves','then','there','there\'s','these','they','they\'d','they\'ll','they\'re','they\'ve','this','those','through','to','too',
    'under','until','up','us',
    'very',
    'was','wasn\'t','we','we\'d','we\'ll','we\'re','we\'ve','were','weren\'t','what','what\'s','when','when\'s','where','where\'s','which','while','who','who\'s','whom','why','why\'s','will','with','won\'t','would','wouldn\'t',
    'you','you\'d','you\'ll','you\'re','you\'ve','your','yours','yourself','yourselves',
    // interjections
    'ah','alas','dear','eh','er','ew','gosh','hmm','huh','hurrah','meh','oh','oops','ouch','phew','psst','ugh','wow','yay',
    // water / filler
    'actually','basically','literally','really','quite','rather','somewhat','simply','just','almost','maybe','perhaps','probably','certainly','definitely','surely','indeed','still','already','yet','even','only','also','too','as','like','well','anyway','anyhow','so','then','thus','therefore','hence','furthermore','moreover','however','nevertheless','although','though','because','since','while','whereas','if','when','unless','until','whether'
  ]);

  const stopWordsRu = new Set([
    'и','в','не','на','я','он','что','с','как','а','то','все','она','так','его','но','да','ты','к','у','же','вы','за','бы','по','только','ее','мне','было','вот','от','меня','еще','нет','о','из','ему','теперь','когда','даже','ну','вдруг','ли','если','уже','или','ни','быть','был','нее','до','вас','нибудь','опять','уж','вам','ведь','там','потом','себя','ничего','ей','может','они','тут','где','есть','надо','ней','для','мы','тебя','их','чем','была','сам','чтоб','без','будто','чего','раз','тоже','себе','под','будет','ж','тогда','кто','этот','того','потому','этого','какой','совсем','ним','здесь','этом','один','почти','мой','тем','чтобы','нее','сейчас','были','куда','зачем','всех','никогда','можно','при','наконец','два','об','другой','хоть','после','над','больше','тот','через','эти','нас','про','всего','них','какая','много','разве','три','эту','моя','впрочем','хорошо','свою','этой','перед','иногда','лучше','чуть','том','нельзя','такой','им','более','всегда','конечно','всю','между',
    'который','которая','которые','которых','которому','которой','которого','свой','своя','свое','свои','сам','сама','само','сами','весь','вся','всё','все','кто-то','что-то','кто-нибудь','что-нибудь','кое-кто','кое-что','некто','нечто','некого','нечего',
    'без','в','до','для','за','из','к','на','над','о','об','от','перед','по','под','при','про','с','у','через','из-за','из-под',
    'и','да','а','но','или','либо','как','когда','едва','если','потому','так','что','чтобы','хотя','пусть','будто','словно','точно','раз',
    'бы','же','ли','не','ни','даже','ведь','вон','вот','именно','лишь','только','разве','неужели','авось','небось','мол','дескать','вряд','уже','ещё','то','либо','нибудь','кое','таки','ка',
    'а','ай','ах','ба','боже','браво','вон','вот','гм','да','ей-богу','ей','ну','ишь','караул','марш','мерси','на','но','ну','ой','ох','прочь','стоп','тьфу','увы','улюлю','ура','фас','фи','цып','цыц','шабаш','эй','эх',
    'очень','слишком','совсем','просто','прямо','типа','вообще','кстати','значит','собственно','действительно','конечно','безусловно','наверное','вероятно','возможно','видимо','по-видимому','кажется','похоже','пожалуй','практически','фактически','на самом деле','например','также','кроме того','более того','прежде всего','следовательно','таким образом','однако','тем не менее','все-таки','все же','между тем','в то же время','вместе с тем','потому','поэтому','в связи с этим'
  ]);

  function isStopWord(word) {
    const lower = word.toLowerCase();
    if (/[а-яё]/.test(lower)) {
      return stopWordsRu.has(lower);
    } else {
      return stopWordsEn.has(lower);
    }
  }

  // ======================== АНАЛИЗ ЧАСТОТЫ ========================

  function tokenize(text) {
    // разбивает текст на токены: слова (буквы + апостроф/дефис) и остальное
    const tokens = [];
    const regex = /([\p{L}\u0027\u002D]+|[^\p{L}]+)/gu;
    let match;
    while ((match = regex.exec(text)) !== null) {
      const token = match[1];
      const isWord = /[\p{L}]/u.test(token);
      tokens.push({ text: token, isWord });
    }
    return tokens;
  }

  function buildStyledHtml(text) {
    const tokens = tokenize(text);
    // первый проход: подсчёт частот стемов не-стоп-слов
    const freqMap = new Map();
    for (const t of tokens) {
      if (!t.isWord) continue;
      const lower = t.text.toLowerCase();
      if (isStopWord(lower)) continue;
      const stem = stemWord(lower);
      freqMap.set(stem, (freqMap.get(stem) || 0) + 1);
    }
    const maxFreq = freqMap.size ? Math.max(...freqMap.values()) : 0;

    // диапазоны стилей
    const MIN_FONT = 12;
    const MAX_FONT = 36;
    const MIN_WEIGHT = 400;
    const MAX_WEIGHT = 700;

    function freqForToken(word) {
      if (isStopWord(word.toLowerCase())) return 0;
      const stem = stemWord(word.toLowerCase());
      return freqMap.get(stem) || 0;
    }

    let html = '';
    for (const t of tokens) {
      if (!t.isWord) {
        html += escapeHtml(t.text);
        continue;
      }
      const count = freqForToken(t.text);
      let fontSize = MIN_FONT;
      let fontWeight = MIN_WEIGHT;
      if (maxFreq > 0 && count > 0) {
        const ratio = count / maxFreq; // от 1/maxFreq до 1
        fontSize = Math.round(MIN_FONT + (MAX_FONT - MIN_FONT) * ratio);
        fontWeight = Math.round(MIN_WEIGHT + (MAX_WEIGHT - MIN_WEIGHT) * ratio);
      }
      html += `<span style="font-size:${fontSize}px;font-weight:${fontWeight};">${escapeHtml(t.text)}</span>`;
    }
    return html;
  }

  function escapeHtml(str) {
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // ======================== ВСПЛЫВАЮЩЕЕ ОКНО ========================

  let popup = null;
  let lastMouseX = 0, lastMouseY = 0;
  let isSelectionActive = false;
  let debounceTimer = null;

  function createPopup() {
    if (popup) return;
    popup = document.createElement('div');
    popup.id = '__wordfreq_popup';
    popup.style.cssText = `
      position: fixed;
      z-index: 2147483647;
      background: #fff;
      border: 1px solid #aaa;
      border-radius: 6px;
      padding: 12px 14px;
      max-width: 800px;
      max-height: 80vh;
      overflow-y: auto;
      box-shadow: 0 4px 16px rgba(0,0,0,0.2);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      display: none;
      word-break: break-word;
      color: #222;
    `;
    document.body.appendChild(popup);
  }

  function showPopup(html, x, y) {
    if (!popup) createPopup();
    popup.innerHTML = html;
    popup.style.display = 'block';
    positionPopup(x, y);
  }

  function hidePopup() {
    if (popup) popup.style.display = 'none';
  }

  function positionPopup(preferX, preferY) {
    const vw = window.innerWidth;
    const vh = window.innerHeight;
    const rect = popup.getBoundingClientRect();
    const popW = rect.width || 400;
    const popH = rect.height || 200;

    let left = preferX + 10;
    let top = preferY + 10;

    // не вылезаем за правый край
    if (left + popW > vw - 10) {
      left = preferX - popW - 10;
      if (left < 10) left = 10;
    }
    // не вылезаем за нижний край
    if (top + popH > vh - 10) {
      top = preferY - popH - 10;
      if (top < 10) top = 10;
    }
    // финальная подстройка, чтобы всегда в пределах
    left = Math.max(5, Math.min(left, vw - popW - 5));
    top = Math.max(5, Math.min(top, vh - popH - 5));

    popup.style.left = left + 'px';
    popup.style.top = top + 'px';
  }

  // ======================== ОБРАБОТЧИКИ СОБЫТИЙ ========================

  function hasSelection() {
    const sel = window.getSelection();
    return sel && !sel.isCollapsed && sel.toString().trim().length > 0;
  }

  function getParagraphText(pEl) {
    return pEl.textContent || '';
  }

  function getSelectedText() {
    const sel = window.getSelection();
    return sel ? sel.toString() : '';
  }

  // отслеживание мыши
  document.addEventListener('mousemove', e => {
    lastMouseX = e.clientX;
    lastMouseY = e.clientY;
  }, true);

  // наведение на параграф
  document.addEventListener('mouseover', e => {
    if (isSelectionActive) return;
    if (hasSelection()) return;

    const p = e.target.closest('p');
    if (!p) return;

    const text = getParagraphText(p);
    if (!text.trim()) return;

    const html = buildStyledHtml(text);
    showPopup(html, lastMouseX, lastMouseY);
  }, true);

  document.addEventListener('mouseout', e => {
    const p = e.target.closest('p');
    if (p && !p.contains(e.relatedTarget)) {
      hidePopup();
    }
  }, true);

  // обработка выделения
  function handleSelectionChange() {
    if (hasSelection()) {
      isSelectionActive = true;
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        if (!hasSelection()) return;
        const text = getSelectedText();
        if (!text.trim()) return;
        const html = buildStyledHtml(text);
        // позиция около выделения
        const sel = window.getSelection();
        const range = sel.getRangeAt(0);
        const rect = range.getBoundingClientRect();
        let x = rect.left + rect.width / 2;
        let y = rect.bottom + 5;
        if (y + 200 > window.innerHeight) y = rect.top - 200;
        showPopup(html, x, y);
      }, 200);
    } else {
      isSelectionActive = false;
      clearTimeout(debounceTimer);
      hidePopup();
    }
  }

  document.addEventListener('selectionchange', handleSelectionChange);
  document.addEventListener('mouseup', () => {
    if (hasSelection()) {
      isSelectionActive = true;
      clearTimeout(debounceTimer);
      const text = getSelectedText();
      if (!text.trim()) return;
      const html = buildStyledHtml(text);
      const sel = window.getSelection();
      const range = sel.getRangeAt(0);
      const rect = range.getBoundingClientRect();
      let x = rect.left + rect.width / 2;
      let y = rect.bottom + 5;
      if (y + 200 > window.innerHeight) y = rect.top - 200;
      showPopup(html, x, y);
    }
  });

  // скрыть попап при клике вне
  document.addEventListener('click', e => {
    if (popup && !popup.contains(e.target) && !hasSelection()) {
      hidePopup();
    }
  }, true);

  // первоначальное создание
  createPopup();
})();