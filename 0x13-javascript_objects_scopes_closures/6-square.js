#!/usr/bin/node
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const printer = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(printer);
      }
    }
  }
}
module.exports = Square5;
module.exports = Square;
