#!/usr/bin/node
// Script to print and compute factorial of a number

function factorials (x) {
  if (x === 0 || x === 1 || isNaN(x)) {
    return 1;
  } else {
    return (x * factorials(x - 1));
  }
}

console.log(factorials(process.argv[2]));
