const express = require('express');
const request = require('request');
var cors = require('cors');
const bodyParser = require('body-parser');
const logger = require('morgan');
//const Data = require('./data');

const API_PORT = 3001;
const app = express();
app.use(cors());
const router = express.Router();


// (optional) only made for logging and
// bodyParser, parses the request body to be a readable json format
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(logger('dev'));

// this is our get method
// this method fetches all available data in our database
router.get('/isValidEntry', (req, res) => {
  
  return res.json({ success: true});


});

router.get('/genRand', (req,res) => {

	request('http://34.68.230.109:9090/generateNums', function(error,response,body) {
	
		res.json({nums:body});
	
	});
});
router.get('/calculateStats',(req,res) => {
	
	request('http://34.68.230.109:9090/calculateStats?'+req.query.allNums, function(error,response,body){
		var result = body.split(",");
		var mean,variance,stddev=0.0;
		var median=0;
		mean = parseFloat(result[0].split(":")[1]);
		median = parseInt(result[1].split(":")[1]);
		variance = parseFloat(result[2].split(":")[1]);
		stddev = parseFloat(result[3].split(":")[1]);
		res.json({mean:mean,median:median,variance:variance,stddev:stddev});
	});

});



// append /api for our http requests
app.use('/api', router);

// launch our backend into a port
app.listen(API_PORT, () => console.log(`LISTENING ON PORT ${API_PORT}`));
