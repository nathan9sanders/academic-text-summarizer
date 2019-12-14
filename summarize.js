$(document).ready(function() {
  $("#submit-text").click(function() {
    var url = "https://chemetoolbox.com/summarize";

    var article = {
      "text": $("#text-box").val()
    };
    console.log(article["text"]);

    article = JSON.stringify(article);

    $.ajax({
      type: "POST",
      url: url,
      data: article,
      success: function (data) {
        console.log(data);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
