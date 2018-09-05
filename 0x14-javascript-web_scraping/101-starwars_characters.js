#!/usr/bin/node
const request = require('request');
const episodeId = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeId;

function listOrderedCharacters (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let charDict = {};
      let charList = JSON.parse(body).characters;
      for (let i = 0; i < charList.length; i++) {
        request(charList[i], function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            charDict[i] = JSON.parse(body).name;
          }
          if (charList.length === Object.keys(charDict).length) {
            for (let k = 0; k < Object.keys(charDict).length; k++) {
              console.log(charDict[k]);
            }
          }
        });
      }
    }
  });
}
listOrderedCharacters(url);
