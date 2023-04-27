#!/usr/bin/node
const fl = require('fs');
const rqst = require('request');
rqst(process.argv[2]).pipe(fl.createWriteStream(process.argv[3]));
