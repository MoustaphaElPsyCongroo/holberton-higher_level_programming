#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    const toPrint = c || 'X';

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.height; j++) {
        if (j === this.height - 1) {
          console.log(toPrint);
        } else {
          process.stdout.write(toPrint);
        }
      }
    }
  }
}

module.exports = Square;
