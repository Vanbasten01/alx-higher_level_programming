#!/usr/bin/node
const BaseModel = require('./5-square');

class Square extends BaseModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
