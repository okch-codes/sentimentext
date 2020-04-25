API_URL = "http://127.0.0.1:8080/sentimentext/api/analyze";
var jqxhr = $.get(API_URL, {url: encodeURIComponent(window.location.href)}, function (res) {
    alert("success");
    console.log("CIAO", res);
})
.done(function(res) {
    alert("second success");
    console.log("CIAO", res);
})
.fail(function(res) {
    alert("error");
    console.log("CIAO", res);
})
.always(function(res) {
    alert("finished");
    console.log("CIAO", res);
});