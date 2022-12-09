#!/usr/bin/node
exports.logMe = (function (item) {
  let nbPrinted = -1;

  return function (item) {
    nbPrinted++;
    console.log(`${nbPrinted}: ${item}`);
  };
}());
