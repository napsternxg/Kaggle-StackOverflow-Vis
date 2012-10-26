/**
 * collect data containing sitename, total(questions, answers, comments, tags) on the page: http://data.stackexchange.com/
 * Requires jQuery
 * Open http://data.stackexchange.com/ in either Google Chrome or Firefox or any browser that supports javascript console which allows you to run your script on the web page.
 * Copy pase the script and it will print the full data in JSON format in the console.
 * If you want to make the data pretty just copy paste the data to http://jsonlint.com/ and it will give you the JSON data in a neatly formatted version.
**/

data = [];

$(".site-list > li").each(function(){
obj = {};
obj.name = $(this).find("img").attr("alt");
obj.totalQ = $(this).find(".totalQuestions > .pretty-short").attr("title");
obj.totalA = $(this).find(".totalAnswers > .pretty-short").attr("title");
obj.totalC = $(this).find(".totalComments > .pretty-short").attr("title");
obj.totalT = $(this).find(".totalTags > .pretty-short").attr("title");

data.push(obj);
});

jsonData = JSON.stringify(data);
console.log(jsonData);