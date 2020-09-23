#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let countWedge = 0;
    let films = JSON.parse(body).results;
    for (let i = 0; i < films.length; i++) {
      let charList = films[i].characters;
      for (let j = 0; j < charList.length; j++) {
        if (charList[j] === 'https://swapi.co/api/people/18/' || charList[j] === 'http://swapi.co/api/people/18/') {
          countWedge += 1;
        }
      }
    }
    console.log(countWedge);
  }
});
