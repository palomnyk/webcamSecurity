var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('mainPage', { title: 'Database search: Rosaceae' });
});

module.exports = router;
