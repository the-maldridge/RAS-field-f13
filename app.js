var fs = require('fs');

var express = require('express');
var app = express();

function loadDB() {
    var file = __dirname + '/match.db';

    fs.readFile(file, 'utf8', parseJSON);

}

function parseJSON(err, data){ 
    if (err) {
	console.log('Error loading json: ' + err);
    }
    _data=JSON.parse(data);
    console.log('JSON loaded: ' + _data);
}

function dumpdb(req, res) {
    res.send(JSON.stringify(_data) + " data concludes");
}

app.use(express.compress());
app.use('/static', express.static(__dirname + '/static'));
loadDB();
app.get('/jsondump', dumpdb);


app.listen(process.env.PORT || 3000);
console.log("Server started on port: " + (process.env.PORT || 3000));
