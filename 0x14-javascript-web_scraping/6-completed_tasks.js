#!/usr/bin/node
// A script to get status code
const request = require('request');
const base = process.argv[2];
const res = {};
request.get(base, (error, response, body) => {
  if (response && !error) {
    const result = JSON.parse(body);
    let i = 0;
    while (i < result.length) {
      if (result[i]['userId'] in res) {
	if (result[i]['completed'])
        res[result[i]['userId']]++;
      } else {
        if (result[i]['completed'])
        res[result[i]['userId']] = 1;
      }
    i++;
    }
  }
    console.log(res);
});
