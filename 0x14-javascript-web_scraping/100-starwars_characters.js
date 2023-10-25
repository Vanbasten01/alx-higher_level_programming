#!/usr/bin/node

const args = process.argv;
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + args[2], (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    const characters = JSON.parse(body).characters;
    characters.forEach(character => {
      request(character, (err, code, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
