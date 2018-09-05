#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films';
let id = process.argv[2];

function printTitle (url, id) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let jsonDict = JSON.parse(body).results;
      for (let i = 0; i < Object.keys(jsonDict).length; i++) {
        let res = jsonDict[i];
        if (res.episode_id === parseInt(id)) {
          console.log(res.title);
        }
      }
    }
  });
}
printTitle(url, id);
