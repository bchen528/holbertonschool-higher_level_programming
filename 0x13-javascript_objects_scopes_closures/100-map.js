#!/usr/bin/node
var list = require('./100-data').list;

console.log(list);
const map1 = list.map((x, index) => x * index);
console.log(map1);
