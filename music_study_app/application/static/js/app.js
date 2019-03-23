const api_url = "http://localhost:8000/api"
var question_params;

function populateQuestion(data){
    const answer_letters = ["a", "b", "c", "d"]
    $("#new_question").hide();
    $("#submit_answer").show();
    $("#question").html(data.question);
    $("#answer_options").empty();
    data.answer_options.forEach((answer, index) => {
      $("#answer_options").append(`<input type="radio" name="answer" value="${answer}">${answer}</input>`)
    })

}

function getNewQuestion(){
    $.get( api_url + "/question", function( data ) {
      question_params = data.question_params;
    populateQuestion(data);
    });
}

function displayAnswer(data){
  $("#new_question").show();
  $("#submit_answer").hide();
  $("#question").empty();
  $("#answer_options").empty();
  if(data.user_correct){
      $("#answer_display").html("You are correct");
  }else{
      $("#answer_display").html("You are incorrect");
  }
}

function setUpForPost(){
  const csrftoken = Cookies.get('csrftoken');
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
  });
}

function submitAnswer(){
    setUpForPost();
    const user_answer = $('input[name=answer]:checked').val();
    const payload = Object.assign(question_params, {user_answer})
    $.post(`${api_url}/answer`, payload)
        .done((data) => displayAnswer(data))

}




$('#new_question').click(function(){
  getNewQuestion();
});

$('#submit_answer').click(function(){
  submitAnswer();
});


$(document).ready(getNewQuestion());


