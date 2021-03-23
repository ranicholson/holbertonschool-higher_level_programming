#!/usr/bin/node
// Script to search 2nd biggest integer in list of arguments

const srt2 = [];
if (process.argv.length <= 3) {
  console.log('0');
} else {
  for (let x = 2; x < process.argv.length; x++) {
    srt2.push(process.argv[x]);
  }
  srt2.sort(function (a, b) { return b - a; });
  console.log(srt2[1]);
}
