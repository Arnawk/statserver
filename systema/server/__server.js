const express=require('express');
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
  
  return res.json({ success: true, data: req });


});

router.get('/testCalls', function (req, res) { return res.json({1:0}) });

// append /api for our http requests
app.use('/api', router);

// launch our backend into a port
app.listen(API_PORT, () => console.log(`LISTENING ON PORT ${API_PORT}`));


