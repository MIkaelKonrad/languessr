window.onload = function() {
    if(localStorage.getItem('roundNumber') == null ){
      document.getElementById('Rnd#').innerText = "Round: 1/5 \n Score: 0"  
    }else{
      document.getElementById('Rnd#').innerText = "Round: " + localStorage.getItem('roundNumber') + "/5 \n Score: " + localStorage.getItem('totalScore');
    }
    }