const api_url = "http://localhost:8000/api"


$('#new_question').click(function(){
  $.get( api_url + "/question", function( data ) {
  console.log(data)
});
});
