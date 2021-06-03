#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let myStr = '';
    for (let x = 0; x < this.width; x++) {
      myStr += 'X';
    } for (let y = 0; y < this.height; y++) {
      console.log(myStr);
    }
  }
}
module.exports = Rectangle;
