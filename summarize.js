$().ready(function() {
  $("#text").html("Text added by jQuery code.");
});

$(document).ready(function() {
  $('form').submit(function (e) {
    e.preventDefault(); // block the traditional submission of the form.
      var url = "https://processintegrator.herokuapp.com/"; // send the form data here.

      var article = {
        "text": 
      };

      article = JSON.stringify(process_data);

      $.ajax({
          type: "POST",
          url: url,
          data: article,
          success: function (data) {
            
          },
          error: function(error) {
            console.log(error);
          }
      });
  });
});