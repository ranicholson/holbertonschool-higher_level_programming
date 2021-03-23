#!/usr/bin/node
// Function that reverses a list

exports.esrever = function (list) {
  return list.map(list.pop, [...list]);
};
