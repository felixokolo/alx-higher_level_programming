#!/usr/bin/node
const fs = require('fs');
const files = process.argv[2];
console.log(files);
fs.readFile(files, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
