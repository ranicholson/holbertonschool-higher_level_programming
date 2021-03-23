#!/usr/bin/node
// Function that prints number of arguments printed and values

let numLogs = 0;
exports.logMe = function (item) {
  console.log(numLogs + ': ' + item);
  numLogs += 1;
};
