/* Where to write results in the html page */
let status = document.getElementById('status');
let prediction = document.getElementById('prediction');

/* Generic Sensors API */
let sensor = new Accelerometer({frequency: 0.5});

/* Global variables */
var moves = 0;                                            //counter for movement values
var walking = false;                                      //prediction value
var counter = 0;                                          //when this counter reaches 10 we will make a prediction

sensor.start();                                           //start the accelerometer
/* We make the prediction every 10 messages */
sensor.onreading = () => {
  
  console.log("Acceleration along X-axis: " + sensor.x);
  console.log("Acceleration along Y-axis: " + sensor.y);
  console.log("Acceleration along Z-axis: " + sensor.z);
  var x = sensor.x;
  var y = sensor.y;
  var z = sensor.z;
  /* Compute sum of the absolute values */
  var absolute = Math.abs(x) + Math.abs(y) + Math.abs(z);
  var moving = false;     //initially we set the current moving to false
  
  if (absolute > 13.5){
    moves = moves + 1;    //increment moves
    moving = true;        //set current moving to true
  }
  if(counter == 10){      //compute prediction
    if(moves > counter - counter/5){    //if more than 8 moves in this case ar detected then user is walking
        walking = true;
        moves = 0;                      //reset moves
    }
    else{
        walking = false;                //user is not walking
    }
    counter = 0;
  }
  if(counter != 0)
    counter = counter + 1;              //increment counter if it has not reached the end
  
  /* Update prediction value in HTML */
  if(walking){
    prediction.innerHTML = 'It seems that you are walking';
  }
  else{
    prediction.innerHTML = 'It seems that you are not moving';
  }

  /* Update sensor values in HTML */
  status.innerHTML = 'x: ' + sensor.x + '<br> y: ' + sensor.y + '<br> z: ' + sensor.z + '<br> Moving: ' + moving.toString() + '<br> Walking: '+ walking.toString();

  /* Send data to ThingsBoard */
  const Http = new XMLHttpRequest();
  const url='https://demo.thingsboard.io/api/v1/TOKEN/telemetry';
  Http.open("POST",url);
  Http.send('{\"x\":\" ' + sensor.x +'\", \"y\":'+ sensor.y +', \"z\": '+ sensor.z + ', \"Moving\":'+ moving.toString() + ', \"Walking\":'+walking.toString() +'}');
}

sensor.onerror = event => console.log(event.error.name, event.error.message);   //debug

/*{"key1":"value1", "key2":true, "key3": 3.0, "key4": 4}*/
/*https://demo.thingsboard.io/api/v1/TOKEN/telemetry*/
/*https://host:port/api/v1/$ACCESS_TOKEN/telemetry*/