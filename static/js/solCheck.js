/* The Js Code below computes the number of points achieved by the player as well as 
    displaying those points and the distance between guess location and solution location */

if (parseFloat(localStorage.getItem('accuracyGuess'))>1) {
    window.onload = function() {
      var score =  Math.round(5000*(((15000-parseFloat(localStorage.getItem('accuracyGuess')))/15000)**6));
      var distance = Math.round(parseFloat(localStorage.getItem('accuracyGuess')));
      document.getElementById('distanceCount').innerText = "Distance: \n " + distance + ' km';
      document.getElementById('scoreCount').innerText = 'Score: \n' + score;
      localStorage.setItem('totalScore',parseFloat(localStorage.getItem('totalScore')) + score);
      localStorage.setItem('totalDistance',parseFloat(localStorage.getItem('totalDistance'))+distance);
      };
  } else{ 
    window.onload = function() {
      var score = 5000;
      document.getElementById('distanceCount').innerText = "Distance: \n " + Math.round(parseFloat(localStorage.getItem('accuracyGuess'))*1000) + " m";
      document.getElementById('scoreCount').innerText = 'Score: \n 5000'
      localStorage.setItem('totalScore', parseFloat(localStorage.getItem('totalScore')) + score);
      console.log(localStorage.getItem('totalScore'));
      }
  }