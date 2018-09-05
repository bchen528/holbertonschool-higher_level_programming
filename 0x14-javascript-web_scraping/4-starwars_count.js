#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

function numAppearances (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let count = 0;
      let hasId = /18/;
      let resList = JSON.parse(body).results;
      for (let i = 0; i < resList.length; i++) {
        let charList = resList[i].characters;
        for (let j = 0; j < charList.length; j++) {
          if (hasId.test(charList[j]) === true) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
numAppearances(url);
