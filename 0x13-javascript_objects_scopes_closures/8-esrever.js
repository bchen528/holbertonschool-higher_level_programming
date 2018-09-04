#!/usr/bin/node
exports.esrever = function (list) {
  let temp = 0;
  for (let i = 0; i < list.length; i++) {
    let right = list.length - 1 - i;
    if (i < right) {
      temp = list[i];
      list[i] = list[right];
      list[right] = temp;
    }
  }
  return list;
};
