#!/usr/bin/node
let fs = require('fs');
let fileA = process.argv[2];
let fileB = process.argv[3];
let fileC = process.argv[4];
function concat (fileA, fileB, fileC) {
  fs.readFile(fileA, function (err, data) {
    if (err) {
      console.log(err.stack);
    }
    fs.appendFile(fileC, data);
  });
  fs.readFile(fileB, function (err, data) {
    if (err) {
      console.log(err.stack);
    }
    fs.appendFile(fileC, data);
  });
}
concat(fileA, fileB, fileC);
