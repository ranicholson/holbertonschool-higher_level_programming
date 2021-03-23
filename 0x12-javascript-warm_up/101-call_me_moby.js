#!/usr/bin/node
// Function that executes a function x times

exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};
