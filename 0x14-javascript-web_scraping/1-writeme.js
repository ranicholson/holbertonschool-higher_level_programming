#!/usr/bin/node
// Script to read file and print contents

const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], err => {
  if (err) {
    console.log(err);
  }
});
