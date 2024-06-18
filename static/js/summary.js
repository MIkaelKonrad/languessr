
/* The function below adjusts the score bar to the achieved score */
window.onload = function() {
    var fillpercent = Math.round(parseFloat(localStorage.getItem('totalScore'))/250);
    document.getElementById('pointBar').style.width= fillpercent.toString() + "%";
    document.getElementById('pointBar').innerText = localStorage.getItem('totalScore').toString() +'/25000';
}




/* The below code adjusts the text below the score bar to the score acieved*/
localStorage.setItem('roundNumber',1);
    document.getElementById('totalSc').innerText = 'Your total score was ' + localStorage.getItem('totalScore').toString()
                 +' and you were off by a total of ' + localStorage.getItem('totalDistance') + ' km.';






var array= localStorage.getItem('guessInfo').split(',');
let map;
/* The while loop below is to compute max and min lat (resp. lng) of both guesses and solutions.
 this is later used to determine the center of the map */
var latMax = parseFloat(array[1]);
var latMin = parseFloat(array[1]);
var lngMax = parseFloat(array[2]);
var lngMin = parseFloat(array[2]);
var j = 1;
while (j<10){
    if (parseFloat(array[2*j+1])> latMax){
        latMax = parseFloat(array[2*j+1]);
    }else if(parseFloat(array[2*j+1])< latMin){
        latMin = parseFloat(array[2*j+1]);
    }
    if(parseFloat(array[2*j+2])> lngMax){
        lngMax = parseFloat(array[2*j+2]);
    }else if(parseFloat(array[2*j+2])< lngMin){
        lngMin = parseFloat(array[2*j+2]);
    }
    j= j+1;
};

/* The function below generates the map displayed in in the center of the screen.  */ 
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: (latMax + latMin)/2, lng: (lngMax + lngMin)/2 },
        zoom: 4
    });
    /* The while loop below cycles through all of the 5 guesses made by the user. */
    var i = 0;
    while(i<5){
        /* Below we build a line connecting the i+1 th guess with the i+1 th solution, 
            using the Polyline class from the google maps API*/
        var connectingLine = new google.maps.Polyline({
            path: [ {lat: parseFloat(array[i*4 + 1]) , lng: parseFloat(array[i*4 + 2])},
                         {lat: parseFloat(array[i*4 + 3]) , lng: parseFloat(array[i*4 + 4])} ],
            geodesic: true,
            strokeColor: "#000000",
            strokeOpacity: 1.0,
            strokeWeight: 1.5,
        });
        connectingLine.setMap(map);
        /* guessIcon and solIcon are objects, which can be used as Icons for the markers */ 
        const guessIcon = {
            url: '/static/images/GuessIcon'+(i+1) +'.png', // url
            scaledSize: new google.maps.Size(30, 30), // scaled size
            origin: new google.maps.Point(0,0), // origin
            anchor: new google.maps.Point(15, 15) // anchor
        };
        const solIcon = {
            url: '/static/images/solIcon'+(i+1) +'.png', // url
            scaledSize: new google.maps.Size(30, 30), // scaled size
            origin: new google.maps.Point(0,0), // origin
            anchor: new google.maps.Point(15, 15) // anchor
        };
        /* Markers for i+1 th guess (resp. sol) as instance of Marker class from the googlemaps API */
        var markerGuess = new google.maps.Marker({
            map: map,
            position: {lat: parseFloat(array[i*4 + 1]) , lng: parseFloat(array[i*4 + 2])},
            draggable: false,
            icon: guessIcon
        });
        var markerSol = new google.maps.Marker({
            map: map,
            position: {lat: parseFloat(array[i*4 + 3]) , lng: parseFloat(array[i*4 + 4])},
            draggable: false,
            icon: solIcon
        });
        i=i+1;
    }
}