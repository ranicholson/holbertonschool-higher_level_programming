#!/usr/bin/node
// Script to read file and print contents

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  console.log(err || data);
});
