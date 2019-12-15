$(document).ready(function() {
  $("#submit-text").click(function() {
    var url = "http://127.0.0.1:5000/summarize";

    var article = {
      "text": $("#text-box").val()
    };

    article = JSON.stringify(article);

    $.ajax({
      type: "POST",
      url: url,
      data: article,
      success: function (data) {
        data = JSON.parse(data);
        $("#summary").html(data["summary"]);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
