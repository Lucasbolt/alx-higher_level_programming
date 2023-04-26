#!/usr/bin/node
const fl = require('fs');
fl.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
