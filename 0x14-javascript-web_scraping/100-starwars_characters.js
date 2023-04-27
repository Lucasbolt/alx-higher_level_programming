#!/usr/bin/node

const rqst = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
rsqt.get(url + id, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const i of characters) {
    rsqt.get(i, function (error, res, body) {
      if (error) {
        console.log(error);
      }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
