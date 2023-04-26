#!/usr/bin/node

const rqst = require('request');
rqst.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
