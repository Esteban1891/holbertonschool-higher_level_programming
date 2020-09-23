#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const args = process.argv.slice(2);
const apiUrl = args[0];
const file = args[1];
request(apiUrl).pipe(fs.createWriteStream(file));
