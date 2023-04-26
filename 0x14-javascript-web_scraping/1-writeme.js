#!/usr/bin/node
const fl = require('fs');
fl.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
