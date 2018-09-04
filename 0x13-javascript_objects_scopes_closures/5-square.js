#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle);
    } else if (w && h) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let y = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(y.repeat(this.width));
    }
  }

  rotate () {
    let i = this.width;
    this.width = this.height;
    this.height = i;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
