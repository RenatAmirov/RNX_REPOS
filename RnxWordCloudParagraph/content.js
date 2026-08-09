(function () {
  'use strict';

  // ========== СТЕММЕРЫ ==========
  // Стеммер Портера для русского языка (упрощённая реализация snowball)
  function russianStemmer(word) {
    word = word.toLowerCase();
    if (word.length < 3) return word;
    const vowels = 'аеиоуыэюя';
    const perfectiveGround = /.*(ив|ивши|ившись|ыв|ывши|ывшись)$/;
    const reflexive = /(ся|сь)$/;
    const adjective = /(ее|ие|ые|ое|ими|ыми|ей|ий|ый|ой|ем|им|ым|ом|его|ого|ему|ому|их|ых|ую|юю|ая|яя|ою|ею)$/;
    const participle = /(ивш|ывш|ующ)$/;
    const verb = /(ила|ыла|ена|ейте|уйте|ите|или|ыли|ей|уй|ил|ыл|им|ым|ен|ило|ыло|ено|ят|ует|уют|ит|ыт|ены|ить|ыть|ишь|ую|ю)$/;
    const noun = /(а|ев|ов|ие|ье|е|иями|ями|ами|еи|ии|и|ией|ей|ой|ий|й|иям|ям|ием|ем|ам|ом|о|у|ах|иях|ях|ы|ь|ию|ью|ю|ия|ья|я)$/;
    const superlative = /(ейше|ейш)$/;
    const derivational = /(ост|ость)$/;
    let stem = word;
    // Шаг 1: удаление окончаний совершенного вида
    stem = stem.replace(perfectiveGround, '');
    // Рефлексивность
    stem = stem.replace(reflexive, '');
    // Прилагательные
    if (adjective.test(stem)) {
      stem = stem.replace(adjective, '');
      stem = stem.replace(participle, '');
    } else {
      // Причастия
      stem = stem.replace(participle, '');
      // Глаголы
      if (verb.test(stem)) {
        stem = stem.replace(verb, '');
      } else {
        // Существительные
        stem = stem.replace(noun, '');
      }
    }
    // Шаг 2: удаление суффикса "и"
    stem = stem.replace(/и$/, '');
    // Шаг 3: удаление превосходной степени
    stem = stem.replace(superlative, '');
    // Шаг 4: удаление деривационных суффиксов
    stem = stem.replace(derivational, '');
    // Удаление мягкого знака
    stem = stem.replace(/ь$/, '');
    // Если основа слишком короткая, возвращаем исходное слово
    return stem.length > 2 ? stem : word;
  }

  // Стеммер Портера для английского языка
  function englishStemmer(word) {
    word = word.toLowerCase();
    if (word.length < 3) return word;
    // Шаг 1a
    word = word.replace(/sses$/, 'ss').replace(/ies$/, 'i').replace(/ss$/, 'ss').replace(/s$/, '');
    // Шаг 1b
    let flag = false;
    if (/(eed|eedly)$/.test(word)) {
      const stem = word.replace(/(eed|eedly)$/, '');
      if (stem.length > 1) {
        word = stem + 'ee';
      }
    } else if (/(ed|edly|ing|ingly)$/.test(word)) {
      const stem = word.replace(/(ed|edly|ing|ingly)$/, '');
      if (stem.length > 1) {
        word = stem;
        flag = true;
      }
    }
    if (flag) {
      if (/(at|bl|iz)$/.test(word)) {
        word += 'e';
      } else if (/(bb|dd|ff|gg|mm|nn|pp|rr|tt)$/.test(word)) {
        word = word.slice(0, -1);
      } else if (/[^aeiouylsz][aeiou][^aeiouwxy]$/.test(word) && word.length > 2) {
        word += 'e';
      }
    }
    // Шаг 1c
    word = word.replace(/y$/, 'i');
    // Остальные шаги (2-5) для простоты опущены, это даёт приемлемый результат
    return word;
  }

  // Определение языка: если больше кириллических букв, русский, иначе английский
  function detectLanguage(text) {
    const cyrillicCount = (text.match(/[а-яё]/gi) || []).length;
    const latinCount = (text.match(/[a-z]/gi) || []).length;
    return cyrillicCount >= latinCount ? 'ru' : 'en';
  }

  // ========== СТОП-СЛОВА (местоимения, междометия, предлоги, союзы, водные) ==========
  const stopWordsRU = new Set([
    'и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'но',
    'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от', 'меня',
    'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг', 'ли', 'если', 'уже', 'или',
    'быть', 'был', 'него', 'вас', 'вам', 'себя', 'один', 'как', 'уже', 'до', 'мой', 'это', 'чтоб', 'потому',
    'себе', 'тобой', 'нам', 'ними', 'тем', 'чем', 'где', 'весь', 'там', 'тут', 'также', 'ни', 'каждый',
    'этот', 'тот', 'все', 'мой', 'твой', 'свой', 'его', 'её', 'их', 'мы', 'вы', 'они', 'кто', 'кого', 'кому',
    'кем', 'ком', 'что', 'чего', 'чему', 'чем', 'чём', 'который', 'которая', 'которые', 'этот', 'эта', 'эти',
    'тот', 'та', 'те', 'такой', 'такая', 'такие', 'сам', 'сама', 'сами', 'весь', 'вся', 'всё', 'все',
    'любой', 'всякий', 'другой', 'какой-то', 'некто', 'нечто', 'несколько', 'много', 'мало', 'более',
    'менее', 'очень', 'весьма', 'почти', 'совсем', 'тоже', 'ещё', 'уже', 'просто', 'например', 'ах', 'ох',
    'эх', 'ой', 'ай', 'увы', 'гм', 'хм', 'ну', 'ой-ой', 'ого', 'фи', 'фу', 'ба', 'ура', 'браво',
    'здравствуйте', 'привет', 'пока', 'спасибо', 'пожалуйста', 'извините', 'будьте', 'вроде', 'типа', 'блин'
  ]);

  const stopWordsEN = new Set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves',
    'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their',
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about',
    'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
    'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when',
    'where', 'why', 'how', 'all', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should',
    'now', 'll', 're', 've', 'm', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn',
    'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn', 'hello', 'hi', 'hey',
    'oh', 'ah', 'wow', 'oops', 'hm', 'hmm', 'err', 'uh', 'yeah', 'yes', 'no', 'please', 'thanks', 'sorry'
  ]);

  // ========== ТОКЕНИЗАЦИЯ И АНАЛИЗ ==========
  function tokenize(text) {
    return text.match(/[а-яёa-z0-9]+(?:-[а-яёa-z0-9]+)*/gi) || [];
  }

  function analyzeText(text) {
    const lang = detectLanguage(text);
    const stemmer = lang === 'ru' ? russianStemmer : englishStemmer;
    const stopSet = lang === 'ru' ? stopWordsRU : stopWordsEN;

    const words = tokenize(text);
    const totalWords = words.length;
    let stopWordCount = 0;

    const freqMap = new Map(); // корень -> count
    const wordDetails = [];    // { original, lower, isStop, stem, freq }

    for (let w of words) {
      const lower = w.toLowerCase();
      const isStop = stopSet.has(lower) || lower.length <= 1;
      if (isStop) stopWordCount++;
      const stem = isStop ? lower : stemmer(lower);
      if (!isStop) {
        freqMap.set(stem, (freqMap.get(stem) || 0) + 1);
      }
      wordDetails.push({
        original: w,
        lower: lower,
        isStop: isStop,
        stem: stem,
        freq: 0 // будет заполнено позже
      });
    }

    const maxFreq = freqMap.size ? Math.max(...freqMap.values()) : 0;

    // Заполняем freq для нестоп-слов
    for (let detail of wordDetails) {
      if (!detail.isStop) {
        detail.freq = freqMap.get(detail.stem) || 0;
      } else {
        detail.freq = 0;
      }
    }

    const waterPercent = totalWords ? Math.round((stopWordCount / totalWords) * 100) : 0;
    const topKeyWords = [...freqMap.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([stem, count]) => ({ stem, count, percent: Math.round((count / totalWords) * 100) }));

    return {
      words: wordDetails,
      totalWords,
      stopWordCount,
      waterPercent,
      maxFreq,
      topKeyWords,
      lang
    };
  }

  // ========== ГЕНЕРАЦИЯ HTML ТУЛТИПА ==========
  function generateTooltipHTML(analysis) {
    const { words, waterPercent, maxFreq, topKeyWords } = analysis;
    const baseFontSize = 16;
    const maxFontSize = 36;
    const minWeight = 400;
    const maxWeight = 900;

    let html = `<div class="tooltip-meta">Водность: ${waterPercent}% | Ключевые слова: `;
    html += topKeyWords.map(k => `${k.stem} (${k.percent}%)`).join(', ') + '</div>';

    for (let w of words) {
      let fontSize = baseFontSize;
      let fontWeight = minWeight;
      if (!w.isStop && maxFreq > 0) {
        const ratio = maxFreq > 1 ? (w.freq - 1) / (maxFreq - 1) : 0;
        fontSize = baseFontSize + (maxFontSize - baseFontSize) * ratio;
        fontWeight = minWeight + (maxWeight - minWeight) * ratio;
      }
      html += `<span class="word-span" style="font-size:${fontSize}px;font-weight:${fontWeight};">${escapeHTML(w.original)}</span> `;
    }
    return html;
  }

  function escapeHTML(str) {
    const div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
  }

  // ========== УПРАВЛЕНИЕ ТУЛТИПОМ ==========
  const tooltip = document.createElement('div');
  tooltip.id = 'wordcloud-tooltip';
  document.body.appendChild(tooltip);

  let currentTooltipType = null; // 'paragraph' или 'selection'

  function showTooltip(html, x, y, type) {
    tooltip.innerHTML = html;
    tooltip.style.display = 'block';
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
    currentTooltipType = type;
  }

  function moveTooltip(x, y) {
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
  }

  function hideTooltip() {
    tooltip.style.display = 'none';
    tooltip.innerHTML = '';
    currentTooltipType = null;
  }

  // Проверка выделения
  function hasSelection() {
    const sel = window.getSelection();
    return sel && sel.toString().trim().length > 0;
  }

  // Обработчики
  function onParagraphMouseOver(e) {
    const target = e.target.closest('p');
    if (!target || hasSelection()) return;
    const text = target.innerText;
    if (!text.trim()) return;
    const analysis = analyzeText(text);
    const html = generateTooltipHTML(analysis);
    showTooltip(html, e.clientX + 15, e.clientY + 15, 'paragraph');
  }

  function onParagraphMouseMove(e) {
    if (currentTooltipType === 'paragraph') {
      moveTooltip(e.clientX + 15, e.clientY + 15);
    }
  }

  function onParagraphMouseOut(e) {
    if (currentTooltipType === 'paragraph') {
      hideTooltip();
    }
  }

  function onMouseUp(e) {
    setTimeout(() => {
      const sel = window.getSelection();
      if (!sel || sel.toString().trim().length === 0) {
        if (currentTooltipType === 'selection') hideTooltip();
        return;
      }
      const text = sel.toString();
      const analysis = analyzeText(text);
      const html = generateTooltipHTML(analysis);
      const rect = sel.getRangeAt(0).getBoundingClientRect();
      const x = Math.min(rect.left + 10, window.innerWidth - 420);
      const y = rect.bottom + 10;
      showTooltip(html, x, y, 'selection');
    }, 10);
  }

  function onSelectionChange() {
    if (!hasSelection() && currentTooltipType === 'selection') {
      hideTooltip();
    }
  }

  // Скрытие при клике вне тултипа
  function onClick(e) {
    if (!tooltip.contains(e.target) && currentTooltipType) {
      hideTooltip();
    }
  }

  // Делегирование событий
  document.addEventListener('mouseover', onParagraphMouseOver, true);
  document.addEventListener('mousemove', onParagraphMouseMove, true);
  document.addEventListener('mouseout', onParagraphMouseOut, true);
  document.addEventListener('mouseup', onMouseUp);
  document.addEventListener('selectionchange', onSelectionChange);
  document.addEventListener('click', onClick);

  // Сброс при скролле (чтобы не мешал)
  window.addEventListener('scroll', () => {
    if (currentTooltipType) hideTooltip();
  }, true);

})();