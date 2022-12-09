#!/usr/bin/node
exports.esrever = function (list) {
  const rev = list.sort(elem => -1);

  return rev;
};
