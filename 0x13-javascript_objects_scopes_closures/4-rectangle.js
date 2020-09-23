#!/usr/bin/node
const Rectangle = class {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      w = undefined;
      h = undefined;
    }
    if (w !== undefined && h !== undefined) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const printer = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(printer);
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;
