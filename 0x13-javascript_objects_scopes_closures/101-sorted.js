#!/usr/bin/node
let oldDict = require('./101-data.js').dict;
let newDict = {};
Object.keys(oldDict).forEach(function (key) {
  newDict[oldDict[key]] = [];
});
Object.keys(oldDict).forEach(function (key) {
  if (newDict[oldDict[key]].includes(key) === false) {
    newDict[oldDict[key]].push(key);
  }
});
console.log(newDict);
