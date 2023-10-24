#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const results = JSON.parse(body).results;

  for (const movie in results) {
    for (const character of results[movie].characters) {
      if (character.endsWith('/18/')) {
        count += 1;
      }
    }
  }

  console.log(count);
});
