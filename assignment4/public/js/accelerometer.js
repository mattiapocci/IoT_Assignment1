let status = document.getElementById('status');                                             //where to write the result in html page

let sensor = new Accelerometer({frequency: 0.5});                                           //generic sensors API
sensor.start();                                                                             //start the accelerometer

sensor.onreading = () => {
  status.innerHTML = 'x: ' + sensor.x + '<br> y: ' + sensor.y + '<br> z: ' + sensor.z;
  console.log("Acceleration along X-axis: " + sensor.x);
  console.log("Acceleration along Y-axis: " + sensor.y);
  console.log("Acceleration along Z-axis: " + sensor.z);
  const Http = new XMLHttpRequest();                                                        //instantiate request
  const url='https://demo.thingsboard.io/api/v1/TOKEN/telemetry';                           //CloudAccelerometer url
  Http.open("POST",url);                                                                    //prepare request

  /* ThingsBoard payload should be like this {"key1":"value1", "key2":true, "key3": 3.0, "key4": 4} */
  Http.send('{\"x\":\" ' + sensor.x +'\", \"y\":'+ sensor.y +', \"z\": '+ sensor.z + '}');  //send post request with the data

}

sensor.onerror = event => console.log(event.error.name, event.error.message);               //debug

/*{"key1":"value1", "key2":true, "key3": 3.0, "key4": 4}*/
/*https://demo.thingsboard.io/api/v1/TOKEN/telemetry*/
/*https://host:port/api/v1/$ACCESS_TOKEN/telemetry*/