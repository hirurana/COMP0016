var express = require('express');
var config = require('../public/external_data/ICO.json');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('worldmap', {title: 'ICO World Data'});
});

module.exports = router;
