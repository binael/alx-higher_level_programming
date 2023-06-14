#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c = 'X') {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.height; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
};
