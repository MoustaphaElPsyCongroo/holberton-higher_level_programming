#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const onlyElem = list.filter(elem => elem === searchElement);

  return onlyElem.length || 0;
};
