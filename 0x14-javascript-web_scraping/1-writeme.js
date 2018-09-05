#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let content = process.argv[3];

function writeMe (file, content) {
  fs.writeFile(file, content, function (err) {
    if (err) {
      console.log(err);
    }
  });
}
writeMe(file, content);
