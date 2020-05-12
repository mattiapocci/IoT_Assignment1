let status = document.getElementById('status');

let sensor = new Accelerometer({frequency: 0.5});
sensor.start();

sensor.onreading = () => {
  status.innerHTML = 'x: ' + sensor.x + '<br> y: ' + sensor.y + '<br> z: ' + sensor.z;
  console.log("Acceleration along X-axis: " + sensor.x);
  console.log("Acceleration along Y-axis: " + sensor.y);
  console.log("Acceleration along Z-axis: " + sensor.z);
  const Http = new XMLHttpRequest();
  const url='https://demo.thingsboard.io/api/v1/TOKEN/telemetry';
  Http.open("POST",url);
  Http.send('{\"x\":\" ' + sensor.x +'\", \"y\":'+ sensor.y +', \"z\": '+ sensor.z + '}');

}

sensor.onerror = event => console.log(event.error.name, event.error.message);

/*{"key1":"value1", "key2":true, "key3": 3.0, "key4": 4}*/
/*https://demo.thingsboard.io/api/v1/TOKEN/telemetry*/
/*https://host:port/api/v1/$ACCESS_TOKEN/telemetry*/