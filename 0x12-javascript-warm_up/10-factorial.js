#!/usr/bin/node
function factorialize (n) {
  if (isNaN(n) === true || n === 0) {
    return (1);
  }
  return (n * factorialize(n - 1));
}
console.log(factorialize(parseInt(process.argv[2], 10)));
