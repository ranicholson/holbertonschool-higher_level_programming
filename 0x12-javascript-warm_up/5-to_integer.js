#!/usr/bin/node
// Script to print number passed as argument

if (isNaN(Number(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
