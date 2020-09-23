#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
