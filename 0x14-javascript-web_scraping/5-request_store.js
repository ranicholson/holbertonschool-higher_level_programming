#!/usr/bin/node
// Script that takes contents of a web page and stores it in a FILE

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
