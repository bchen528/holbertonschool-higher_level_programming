#!/usr/bin/node
const x = process.argv[2];
let y = 'X';
if (x && isNaN(x) === false) {
  for (let i = 0; i < x; i++) {
    console.log(y.repeat(x));
  }
} else {
  console.log('Missing size');
}
