#!/usr/bin/node
let i, num, max, secondMax;
if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    num = parseInt(process.argv[i], 10);
    if (i === 2) {
      max = num;
    }
    if (num > max) {
      secondMax = max;
      max = num;
    } else {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
