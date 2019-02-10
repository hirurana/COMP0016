var express = require('express');
var router = express.Router();
var mongodb = require('mongodb');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/list', function(req, res){
  var MongoClient = mongodb.MongoClient;
  var url = 'mongodb://localhost:27017/coffee';
  MongoClient.connect(url, function(err, db){
    if(err){
      console.log('Cannot connect to server', err);
    } else {
      console.log("Successfully connected to server");
      var collection = db.collection('name'); //put correct name of collection

      collection.find({}).toArray(function (err, result) {
      if (err) {
        res.send(err);
      } else if (result.length) {
        res.render('articles',{
        "articles" : result
        });
      } else {
        res.send('Nothing found');
      }
      db.close();
    });
  }
  });
});
module.exports = router;
