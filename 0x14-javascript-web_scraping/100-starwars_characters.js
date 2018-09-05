#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films';
const episodeId = process.argv[2];

function listCharacters (url, episodeId) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      let jsonDict = JSON.parse(body).results;
      for (let i = 0; i < Object.keys(jsonDict).length; i++) {
        let epiDict = jsonDict[i];
        if (epiDict.episode_id === parseInt(episodeId)) {
          let charList = epiDict.characters;
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
      }
    }
  });
}
listCharacters(url, episodeId);
