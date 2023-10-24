#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    const tasks = {};
    for (const task of JSON.parse(body)) {
      if (task.completed) {
        if (tasks[task.userId] === undefined) {
          tasks[task.userId] = 1;
        } else {
          tasks[task.userId]++;
        }
      }
    }
    console.log(tasks);
  }
});
