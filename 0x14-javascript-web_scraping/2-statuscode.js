#!/usr/bin/node
const request = require('request')
const getURL = process.argv[2];
request.get(getURL).on('response', (response) => {
  if (response) {
    console.error('code:', response.statusCode);
  }
});
