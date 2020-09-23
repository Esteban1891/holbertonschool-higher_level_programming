#!/usr/bin/node
exports.converter = function (base) {
  this.base = base;
  function myConverter (num) {
    return num.toString(this.base);
  }
  return myConverter;
};
