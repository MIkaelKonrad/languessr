/* The code below updates the round counding and handles the button links of Page2
 If no round count or roundcount = 5 set roundnuber to 1, else increase roundcount by one*/
var Btn = document.getElementById('NxtRndBtn');
  var a = document.getElementById('attrBtn')

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