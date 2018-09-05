#!/usr/bin/node
const request = require('request');
const url = process.argv[2] + '?completed=true';

function taskDoneCount (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let taskDict = {};
      let res = JSON.parse(body);
      for (let i = 0; i < res.length; i++) {
        taskDict[res[i].userId] = 0;
      }
      for (let j = 0; j < res.length; j++) {
        taskDict[res[j].userId]++;
      }
      console.log(taskDict);
    }
  });
}
taskDoneCount(url);
