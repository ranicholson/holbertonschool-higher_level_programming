#!/usr/bin/node
// Script to request status code

const request = require('request');
request.get(process.argv[2], function (err, r, body) {
  if (err) {
    console.log(err);
  } else {
    let WedgeCount = 0;
    const films = JSON.parse(body).results;
    for (let x = 0; x < films.length; x++) {
      for (let y = 0; y < films[x].characters.length; y++) {
        if (films[x].characters[y].includes('/18/')) {
          WedgeCount++;
          break;
        }
      }
    }
    console.log(WedgeCount);
  }
});
