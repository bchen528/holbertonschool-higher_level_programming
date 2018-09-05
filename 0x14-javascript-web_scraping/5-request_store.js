#!/usr/bin/node
const request = require('request');
let fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

function storeWebpage (url, file) {
  request(url, function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      fs.writeFile(file, body, function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
}
storeWebpage(url, file);
