$('#submit-text').click(function() {
  var url = "https://processintegrator.herokuapp.com/"; // send the form data here.

  var article = {
    "text": $("select#text-input").val()
  };
  console.log(article["text"]);

  article = JSON.stringify(process_data);

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