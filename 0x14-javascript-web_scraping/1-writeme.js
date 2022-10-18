#!/usr/bin/node
const fs = require('fs');
const files = process.argv[2];
const content = process.argv[3];
fs.writeFile(files, content, 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
