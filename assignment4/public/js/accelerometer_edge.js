let status = document.getElementById('status');
let prediction = document.getElementById('prediction');
let sensor = new Accelerometer({frequency: 0.5});
var moves = 0;
var lastMoves = false;
var counter = 0;

sensor.start();

sensor.onreading = () => {
  
  console.log("Acceleration along X-axis: " + sensor.x);
  console.log("Acceleration along Y-axis: " + sensor.y);
  console.log("Acceleration along Z-axis: " + sensor.z);
  var x = sensor.x;
  var y = sensor.y;
  var z = sensor.z;
  var absolute = Math.abs(x) + Math.abs(y) + Math.abs(z);
  var moving = false;
  

  if (absolute > 13.5){
    moves = moves + 1;
    moving = true;
  }
  if(counter == 10){
    if(moves > counter - counter/5){
        lastMoves = true;
        moves = 0;
    }
    else{
        lastMoves = false;
    }
    counter = 0
  }
  counter = counter + 1;
  if(lastMoves){
    prediction.innerHTML = 'It seems that you are walking';
  }
  else{
    prediction.innerHTML = 'It seems that you are not moving'
  }
  status.innerHTML = 'x: ' + sensor.x + '<br> y: ' + sensor.y + '<br> z: ' + sensor.z + '<br> Moving: ' + moving.toString() + '<br> Walking: '+ lastMoves.toString();
  const Http = new XMLHttpRequest();
  const url='https://demo.thingsboard.io/api/v1/TOKEN/telemetry';
  Http.open("POST",url);
  Http.send('{\"x\":\" ' + sensor.x +'\", \"y\":'+ sensor.y +', \"z\": '+ sensor.z + ', \"Moving\":'+ moving.toString() + ', \"Walking\":'+lastMoves.toString() +'}');
}

sensor.onerror = event => console.log(event.error.name, event.error.message);

/*{"key1":"value1", "key2":true, "key3": 3.0, "key4": 4}*/
/*https://demo.thingsboard.io/api/v1/TOKEN/telemetry*/
/*https://host:port/api/v1/$ACCESS_TOKEN/telemetry*/