var express = require('express');
var config = require('../public/external_data/ICO.json');
var router = express.Router();
let {PythonShell} = require('python-shell')
const MongoClient = require('mongodb').MongoClient;

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('worldmap', {title: 'ICO World Data'});
});

router.get('/download', function(req, res) {
    var country_name = req.query.country_name;
    var options = {
        scriptPath: __dirname + '/../public/scripts/',
        args: [country_name]
    };

    var file = __dirname + '/../public/external_data/exported_data.xlsx';
    res.download(file);
    // PythonShell.run('export.py', options, function (err, results) {
    //     if (err) throw err;
    //     // results is an array consisting of messages collected during execution
    //     console.log('results: %j', results);
    // });
});

router.get('/load_maps', function (req, res) {
    MongoClient.connect("mongodb://localhost:27017/coffee", function (err, db) {

         if(err) throw err;

         //Write databse Insert/Update/Query code here..
         db.collection('ico', function (err, collection) {
            collection.find().toArray(function(err, items) {
                if (err) throw err;
                //console.log(items);
		res.send(items);
            });
        });
    });
})
module.exports = router;
