function validateForm() {
    var questions = document.querySelectorAll('.question');
    for (var i = 0; i < questions.length; i++) {
      var radioButtons = questions[i].querySelectorAll('input[type="radio"]');
      var answered = false;
      for (var j = 0; j < radioButtons.length; j++) {
        if (radioButtons[j].checked) {
          answered = true;
          break;
        }
      }
      if (!answered) {
        alert('Пожалуйста, ответьте на все вопросы.');
        return false;
      }
    }
    return true;
  }