#!/usr/bin/node
const request = require('request');
const episodeId = process.argv[2];
const url = 'http://swapi.co/api/films/' + episodeId;

function listCharacters (url) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let charList = JSON.parse(body).characters;
      for (let j = 0; j < charList.length; j++) {
        request(charList[j], function (error, response, body) {
          if (error) {
            console.log(error);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
      }
    }
  });
}
listCharacters(url);
