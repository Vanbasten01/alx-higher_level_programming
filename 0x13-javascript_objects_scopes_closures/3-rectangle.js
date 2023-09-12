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
}

module.exports = Rectangle;
