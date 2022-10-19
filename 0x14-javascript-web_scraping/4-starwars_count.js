#!/usr/bin/node
// A script to get status code
const request = require('request');
const base = process.argv[2];
let res;
let count = 0;
request.get(base + '/?format=json', (error, response, body) => {
  if (response && !error) {
    res = JSON.parse(body);
    let i = 0;
    while (i < res.results.length) {
      let j = 0;
      while (j < res.results[i].characters.length) {
        if (res.results[i].characters[j].includes('/18/')) {
          count = count + 1;
        }
        j++;
      }
      i++;
    }
    console.log(count);
  }
});
