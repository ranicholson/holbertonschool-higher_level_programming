#!/usr/bin/node
// Creating a class square that inherits from rectangle

const Squares = require('./5-square.js');

module.exports = class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      let wid = '';
      for (let y = 0; y < this.width; y++) {
        wid += c;
      }
      console.log(wid);
    }
  }
};
