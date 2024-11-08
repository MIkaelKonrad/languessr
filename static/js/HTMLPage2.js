function sendScore() {
    var score =  Math.round(5000*(((15000-parseFloat(localStorage.getItem('accuracyGuess')))/15000)**6));
    var distance = Math.round(parseFloat(localStorage.getItem('accuracyGuess')));
    var array= localStorage.getItem('guessInfo').split(',');
    console.log(array);
    console.log(array[array.length-3]);
    guessLat = array[array.length-4]
    guessLng = array[array.length-3]
    data =  distance + ":" + score + ":" + guessLat +":" + guessLng ;
    document.getElementById("NxtRndBtn").value = data;
    
    $.ajax({
        url: "/name",
        type: 'POST',
        dataType: "json",
        data: JSON.stringify(data),
    })
    .done(function () {
        console.log("SAVED")
    })
}