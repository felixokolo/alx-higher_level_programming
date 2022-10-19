#!/usr/bin/node
// A script to get status code
const request = require('request');
const id = process.argv[2];
const base1 = 'https://swapi-api.hbtn.io/api/films/';
const base2 = 'https://swapi-api.hbtn.io/api/people/';
let fRes;
request.get(base2 + '?format=json', (error, response, body) => {
  if (response && !error) {
    request.get(base1 + id + '/?format=json', (error, response, body) => {
      if (response && !error) {
        fRes = JSON.parse(body);
        let i = 0;
        while (i < fRes.characters.length) {
          request.get(fRes.characters[i], (error, response, body) => {
            if (response && !error) {
              console.log(JSON.parse(body).name);
            }
          });
          i++;
        }
      }
    });
  }
});
