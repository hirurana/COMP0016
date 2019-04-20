var express = require('express');
var config = require('../public/external_data/dailycoffeenews_with_sentiment.json');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('newsarticles', {title: 'Recent News'});
});

module.exports = router;
