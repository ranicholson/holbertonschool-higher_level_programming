#!/usr/bin/node
// Script to print a square where first arg is size of square

const x = Number(process.argv[2]);
if (isNaN(x)) {
  console.log('Missing Size');
} else {
  let size = '';
  for (let z = 0; z < x; z++) {
    size += 'X';
  }
  for (let y = 0; y < x; y++) {
    console.log(size);
  }
}
