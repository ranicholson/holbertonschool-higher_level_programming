#!/usr/bin/node
// Script to request status code

const request = require('request');
const URLEpisode = 'https://swapi-api.hbtn.io/api/people/18';
const URLfilms = 'https://swapi-api.hbtn.io/api/films/';
request(URLfilms);
request(URLEpisode, function (err, resp, bod) {
  if (err) {
    console.log(err);
  } else {
    const wedgeprof = JSON.parse(bod);
    console.log(wedgeprof.films.length);
  }
});
