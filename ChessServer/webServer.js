var express = require("express");
var app = express();
var bodyParser = require("body-parser");

var urlencodedParser = bodyParser.urlencoded({ extended: false });

console.log(__dirname + "/" + "home.html");

app.use(bodyParser.json());
app.use(express.static("templates"));
var path = require("path"); 
app.get("/", function (req, res) {
  res.sendFile(path.resolve("../") + "/ChessClient" + "/" + "home.html");
});

app.post("/predict", urlencodedParser, function (req, res) {
  var data = req.body;
  var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
  var xhr = new XMLHttpRequest();
  var url = "http://127.0.0.1:5000/predict";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");

  data = JSON.stringify(data);
  console.log("Sending:" + data);
  xhr.send(data);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var json = JSON.parse(xhr.responseText);
      console.log("Python API Response:" + JSON.stringify(json));
      res.send(JSON.stringify(json));
    }
  };
});
var server = app.listen(8081, function () {
  console.log("Server başlatıldı: Link: http://localhost:8081");
});
