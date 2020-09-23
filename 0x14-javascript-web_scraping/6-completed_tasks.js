#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const tasksDict = {};
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    for (let i = 0; i < tasks.length; i++) {
      const key = tasks[i].userId;
      if (tasks[i].completed) {
        if (!(key in tasksDict)) {
          tasksDict[key] = 1;
        } else {
          tasksDict[key] += 1;
        }
      }
    }
  }
  console.log(tasksDict);
});
