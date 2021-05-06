#!/usr/bin/node
// Script to request status code

const request = require('request');
request(process.argv[2], function (err, resp, bod) {
  if (err) {
    console.log(err);
  } else {
    console.log(3);
  }
});
