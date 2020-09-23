#!/usr/bin/node
let fs = require('fs');
let file = process.argv[2];
let stringWrite = process.argv[3];
fs.writeFile(file, stringWrite, 'utf-8', (err) => {
  if (err) console.log(err);
});
