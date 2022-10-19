#!/usr/bin/node
// A script to get status code
const request = require('request');
const id = process.argv[2];
const base = 'https://swapi-api.hbtn.io/api/films/';
let res;
request.get(base + id + '/?format=json', (error, response, body) => {
  if (response && !error) {
    res = JSON.parse(body);
    console.log(res.title);
  }
});
