const express = require('express');
const request = require('request');
var cors = require('cors');
const bodyParser = require('body-parser');
const logger = require('morgan');

const API_PORT = 3001;
const app = express();
app.use(cors());
const router = express.Router();


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(logger('dev'));


var thrift = require('thrift');
var statserver = require('./gen-nodejs/StatServer');
var ttypes = require('./gen-nodejs/statserver_types');
const assert = require('assert');

var transport = thrift.TBufferedTransport;
var protocol = thrift.TBinaryProtocol;

var connection = thrift.createConnection("10.128.0.3", 9090, {
  transport : transport,
  protocol : protocol
});

connection.on('error', function(err) {
  assert(false, err);
});

// Create a Calculator client with the connection
var client = thrift.createClient(statserver, connection);


router.get('/checkSanity', (req,res) => {
       
	
	//res.json({error:JSON.stringify(req.body)});
	var result = 'all okay!'
 	var numList= req.query.allNums.split(',');
	if(numList.length!=10)
		res.json({error:'Please enter 10 numbers'});
	for(var i=0;i<numList.length;i++)
		if(isNaN(numList[i]))
			result = 'Please enter only numbers';
        res.json({error:result});
 
});
router.get( '/calculateStats' , (req, res) => {
	var stats="";
	var allNumbers= req.query.allNums.split(',');
	client.calculateStat(allNumbers, function(err, response) {
  console.log('ping() resp : '+response);
		if (err) {
    console.log("InvalidOperation " + err);
  } else {
    console.log('Whoa? You know how to divide by zero?'+JSON.stringify(response));
	  stats = JSON.stringify(response);
	  res.setHeader('Content-Type', 'application/json');
  	  res.json(response);
  }
  });
	//res.json(stats);

});
router.get('/pingTest', (req,res) => {

        client.ping(function(err, response) {
  console.log('ping() resp : '+response);
               res.json({ping:response});
  });

});

router.get('/genRand', (req,res) => {

        client.generateNums(function(err, response) {
        res.json({nums:response});

        });

});


// append /api for our http requests
app.use('/api', router);

// launch our backend into a port
app.listen(API_PORT, () => console.log(`LISTENING ON PORT ${API_PORT}`));
