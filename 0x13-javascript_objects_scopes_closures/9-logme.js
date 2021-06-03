#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  console.log('%i: %s', count, item);
  count++;
};
