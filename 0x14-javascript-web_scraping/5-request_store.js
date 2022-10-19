#!/usr/bin/node
// A script to get status code
const request = require('request');
const fs = require('fs');
const base = process.argv[2];
const filename = process.argv[3];
request.get(base, (error, response, body) => {
  if (response && !error) {
    fs.writeFile(filename, body, 'utf8', err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
