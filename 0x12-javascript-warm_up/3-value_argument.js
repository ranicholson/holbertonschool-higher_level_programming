#!/usr/bin/node
// Script to print first argument passed

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
