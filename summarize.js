$(document).ready(function() {
  var url = "https://processintegrator.herokuapp.com/"; // send the form data here.

  var article = {
    "text": $("select#text-input").val()
  };
  console.log(article);

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