#!/usr/bin/node
// Creating a class rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let wid = '';
      for (let y = 0; y < this.width; y++) {
        wid += 'X';
      }
      console.log(wid);
    }
  }

  rotate () {
    const wid = this.width;
    this.width = this.height;
    this.height = wid;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
