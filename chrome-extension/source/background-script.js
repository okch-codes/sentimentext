
chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
    if (changeInfo.status == "complete") {
        API_URL = "http://127.0.0.1:8080/sentimentext/api/analyze";
        var jqxhr = $.get(API_URL, { url: tab.url }, function (res) {
            console.log(res);
        })
            .done(function (res) {
                console.log("DONE", res);
                chrome.tabs.sendMessage(tab.id, {text: res});
            })
            .fail(function (res) {
                console.log("FAIL", res);
            })
            .always(function (res) {
                console.log("ALWAYS", res);
            });
    }
});
