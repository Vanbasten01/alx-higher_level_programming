#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let grid = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        grid += 'X';
      }
      console.log(grid);
      grid = '';
    }
  }

  rotate () {
    const a = this.width;
    this.width = this.height;
    this.height = a;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
