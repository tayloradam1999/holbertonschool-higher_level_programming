#!/usr/bin/node
exports.converter = function (base) {
  function Convert (number) {
    return number.toString(base);
  }
  return Convert;
};
