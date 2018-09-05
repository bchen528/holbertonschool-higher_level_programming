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
      let jsonDict = JSON.parse(body).results;
      for (let i = 0; i < Object.keys(jsonDict).length; i++) {
        let res = jsonDict[i].characters;
        for (let j = 0; j < res.length; j++) {
          if (res[j] === id) {
            count++;
          }
        }
      }
      console.log(count);
    }
  });
}
numAppearances(url, id);
