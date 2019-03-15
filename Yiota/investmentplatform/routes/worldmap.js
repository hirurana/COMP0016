var express = require('express');
var config = require('../public/external_data/ICO.json');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('worldmap', {title: 'ICO World Data'});
});

router.get('/download', function(req, res) {
    var file = __dirname + '/../public/external_data/exported_data.xlsx';
    res.download(file);
});

module.exports = router;
