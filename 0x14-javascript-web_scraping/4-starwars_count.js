#!/usr/bin/node
// Script to request status code

const request = require('request');
const URLEpisode = 'https://swapi-api.hbtn.io/api/people/18';
request(URLEpisode, function (err, resp, bod) {
  if (err) {
    console.log(err);
  } else {
    console.log('3');
  }
});
