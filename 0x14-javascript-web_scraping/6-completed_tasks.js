#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function taskDoneCount (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let taskDict = {};
      let taskList = JSON.parse(body);
      for (let i = 0; i < taskList.length; i++) {
        if (taskDict[taskList[i].userId] === undefined) {
          taskDict[taskList[i].userId] = 0;
        }
      }
      for (let j = 0; j < taskList.length; j++) {
        if (taskList[j].completed === true) {
          taskDict[taskList[j].userId]++;
        }
      }
      console.log(taskDict);
    }
  });
}
taskDoneCount(url);
