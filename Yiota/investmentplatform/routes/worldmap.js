var express = require('express');
var config = require('../public/external_data/ICO.json');
var router = express.Router();
let {PythonShell} = require('python-shell')

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
    let pyshell = new PythonShell('export.py', options);
    pyshell.on('message', function (message) {
        console.log(message);
    })
    pyshell.end(function (err,code,signal) {
        if (err) throw err;
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        console.log('finished');
        console.log('finished');
    });
    // PythonShell.run('export.py', options, function (err, results) {
    //     if (err) throw err;
    //     // results is an array consisting of messages collected during execution
    //     console.log('results: %j', results);
    // });


    var file = __dirname + '/../public/external_data/exported_data.xlsx';
    res.download(file);
});

module.exports = router;
