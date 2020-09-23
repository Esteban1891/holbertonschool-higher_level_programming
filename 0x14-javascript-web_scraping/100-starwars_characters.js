#!/usr/bin/node
const request = require('request');
const epId = process.argv[2];
const apiUrl = `https://swapi.co/api/films/${epId}`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const charList = JSON.parse(body).characters;
    for (let i = 0; i < charList.length; i++) {
      request.get(charList[i], (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          const names = JSON.parse(body).name;
          console.log(names);
        }
      });
    }
  }
});
