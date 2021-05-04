#!/usr/bin/node
// Script to request status code

const request = require('request');
const URLEpisode = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(URLEpisode, function (err, resp, bod) {
  console.log(err || JSON.parse(bod).title);
});
