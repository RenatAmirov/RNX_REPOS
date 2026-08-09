chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    // Не редиректим запросы из самого просмотрщика
    if (details.initiator && details.initiator.startsWith('chrome-extension://' + chrome.runtime.id)) {
      return {};
    }
    const viewerUrl = chrome.runtime.getURL('viewer.html') + '?file=' + encodeURIComponent(details.url);
    return { redirectUrl: viewerUrl };
  },
  { urls: ['*://*/*.pdf', '*://*/*.PDF'] },
  ['blocking']
);