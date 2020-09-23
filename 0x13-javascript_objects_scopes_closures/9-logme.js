#!/usr/bin/node
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  function argPrinter () {
    console.log(`${this.count}: ${item}`);
    this.count += 1;
  }
  return argPrinter();
};
