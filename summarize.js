$(document).ready(function() {
  $("#submit-text").click(function() {
    var url = "https://chemetoolbox.com/summarize";

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
