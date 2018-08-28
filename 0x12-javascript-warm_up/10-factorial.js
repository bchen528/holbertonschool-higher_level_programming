#!/usr/bin/node
function getFactorial (n) {
  if (isNaN(n) === true || n === 0) {
    return (1);
  }
  return (n * getFactorial(n - 1));
}
console.log(getFactorial(parseInt(process.argv[2], 10)));
