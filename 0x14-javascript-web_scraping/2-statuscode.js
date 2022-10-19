#!/usr/bin/node
const request = require('request')
const getURL = process.argv[2];
request.get(getURL).on('response', (response) => {
  if (response) {
    console.log('code: ' + response.statusCode);
  }
});
