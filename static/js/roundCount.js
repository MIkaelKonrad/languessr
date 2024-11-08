/* The code below updates the round counding and handles the button links of Page2
 If no round count or roundcount = 5 set roundnuber to 1, else increase roundcount by one*/
var Btn = document.getElementById('NxtRndBtn');
var score =  Math.round(5000*(((15000-parseFloat(localStorage.getItem('accuracyGuess')))/15000)**6));
var distance = Math.round(parseFloat(localStorage.getItem('accuracyGuess')));
 to_send = 'Score:' + score + "; distance:" + distance;
  var a = document.getElementById('attrBtn');
  if(localStorage.getItem('roundNumber')==null) {
      localStorage.setItem('roundNumber', 1);
      Btn.innerText  = 'Next Round';
      a.href = '/';
    }else if(parseInt(localStorage.getItem('roundNumber')) < 5 ){
      localStorage.setItem('roundNumber',parseFloat(localStorage.getItem('roundNumber')) +1);
      Btn.innerText  = 'Next Round';
      a.href = '/';
    }else{
      localStorage.setItem('roundNumber',1);
      Btn.innerText = 'Summary';
      a.href = '/Summary';
    } 

