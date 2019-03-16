var express = require('express');
var router = express.Router();

/* GET coffee page. */
router.get('/', function(req, res, next) {
  res.render('coffee', { title: 'Investment Platform - Coffee' });
});

module.exports = router;
