
    /* Js code which displays a marker both for the sulotion and for the guess made  */
    let map;
    let markersArray=[] ; 
    var abc = false;
    var guessLat = parseFloat(localStorage.getItem("GuessLat"));
    var guessLng = parseFloat(localStorage.getItem("GuessLng"));
    var targetLat = parseFloat(localStorage.getItem("targetLat"));
    var targetLng = parseFloat(localStorage.getItem("targetLng"));
    var array= localStorage.getItem('guessInfo').split(',');
    array.push(guessLat.toString(),guessLng.toString(),targetLat.toString(),targetLng.toString());
    console.log(array);
    localStorage.setItem('guessInfo',array);
    function initMap() {

     /*The If else statement below computes the degree 'Zoomedinness' the map as depending on the accuracy of the guess made
     at the moment there are only three levels of 'Zoomedinness' developping a comtinuous funtion accuracyGuess -> Zoom, is still to do  */
     if (parseFloat(localStorage.getItem('accuracyGuess'))>5000){
        var Zoom =2.3;
      } else if (5000>parseFloat(localStorage.getItem('accuracyGuess'))>1000){
         var Zoom=3
      }else {
         var Zoom=6
      };

      /* Below we create a new instance of the google.maps.Map class centerd at the half way point between guess and solution */
      map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: (guessLat + targetLat)/2, lng: (guessLng+targetLng)/2 },
          zoom: Zoom
        });
      
      /* below we create a new instance of the google.maps.Polyline class this element is visible as geodesic line 
      connecting guess location and solution location. 
      Possibly a non-Geodesic would look better i.e. a line which is straight on the but curved in irl as opposed to line that is straight 
          irl but appears curved on the map.*/
      var connectingLine = new google.maps.Polyline({
          path: [ {lat: guessLat , lng: guessLng}, {lat: targetLat , lng: targetLng} ],
          geodesic: true,
          strokeColor: "#000000",
          strokeOpacity: 1.0,
          strokeWeight: 1.5,
        })
      connectingLine.setMap(map); // displaying the Polyline defined above on the map

        /* The blow objects: 
              GuessFLagIcon: Style of the flag used to indicate the guess of the user
              flagIcon: Style of the flag used to indicate the solution
              markerGuess: Instance of google.maps.Marker class appearing where user made a guess
              markerTarget: Instance of google.maps.Marker class appearing at the location of the solution.
        */
        const GuessFlagIcon = {
          url: '/static/images/GuessFlag_Layer 1.png', // url
          scaledSize: new google.maps.Size(30, 60), // scaled size
          origin: new google.maps.Point(0,0), // origin
          anchor: new google.maps.Point(0, 60) // anchor
        };

        const flagIcon = {
          url: '/static/images/flag_Layer 1.png', // url
          scaledSize: new google.maps.Size(30, 60), // scaled size
          origin: new google.maps.Point(0,0), // origin
          anchor: new google.maps.Point(0, 60) // anchor
        };

        var markerGuess = new google.maps.Marker({
          map: map,
          position: {lat: guessLat , lng: guessLng},
          draggable: true,
          icon: GuessFlagIcon
        });

        var markerTarget = new google.maps.Marker({
          map: map,
          position: {lat: targetLat , lng: targetLng},
          draggable: true,
          icon: flagIcon
        });
    }

    initMap();