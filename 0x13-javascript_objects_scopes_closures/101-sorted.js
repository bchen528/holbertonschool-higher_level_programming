#!/usr/bin/node

let oldDict = require('./101-data.js').dict;
let newDict = {};
Object.keys(oldDict).forEach(function (key) {
  if (newDict[oldDict[key]] === undefined) {
    newDict[oldDict[key]] = [];
  }
  newDict[oldDict[key]].push(key);
});
console.log(newDict);
