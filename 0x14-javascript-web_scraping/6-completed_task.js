#!/usr/bin/node

const rqst = require('request');
const url = process.argv[2];

rqst(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const finished = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.finished === true) {
        if (finished[task.userId] === undefined) {
          finished[task.userId] = 1;
        } else {
          finished[task.userId]++;
        }
      }
    }
    console.log(finished);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
