var http = require('http');
var https = require('https');
var fs = require('fs');
const express = require('express');
const app = express();

// middleware to static resources
app.use(express.static('public'));

https.createServer({
    key: fs.readFileSync('../conf/key.pem'),
    cert: fs.readFileSync('../conf/cert.pem')
  }, app)
  .listen(3000, '192.168.1.148',function () {
    console.log('Https server is listening on port 3000');
})