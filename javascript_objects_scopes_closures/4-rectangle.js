#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let value = 1; value <= this.height; value++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.height, this.width] = [this.width, this.height];
  }

  double () {
    [this.height, this.width] = [this.height * 2, this.width * 2];
  }
};
