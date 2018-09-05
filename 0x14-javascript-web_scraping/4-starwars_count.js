#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const id = 'https://swapi.co/api/people/18/';

function numAppearances (url, id) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let count = 0;
      let resList = JSON.parse(body).results;
      for (let i = 0; i < resList.length; i++) {
        let charList = resList[i].characters;
        for (let j = 0; j < charList.length; j++) {
          if (charList[j] === id) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
numAppearances(url, id);
