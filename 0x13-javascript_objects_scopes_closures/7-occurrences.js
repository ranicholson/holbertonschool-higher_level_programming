#!/usr/bin/node
// Function that returns number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
