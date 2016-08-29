'use strict'

var express  = require('express');
var app = express();

var allplots = 100;
var yourplots = 0;

function initialPlots(allplots,yourplots){
   console.log("There are " + allplots + " in the city");
   console.log("You own " + yourplots + " total");
}
initialPlots(allplots,yourplots);


var port = process.env.PORT || 3030;
app.listen(port);
console.log("App listening on port " + port); 

var startServer = function() {
	    return port
};

module.exports = { startServer: startServer };
