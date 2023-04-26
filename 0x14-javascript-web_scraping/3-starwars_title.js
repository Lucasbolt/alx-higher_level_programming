#!/usr/bin/node

const rqst = require('request');
const epsd = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';

rqst(API_URL + epsd, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
