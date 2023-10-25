#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const users = {};

  JSON.parse(body).forEach(element => {
    if (element.completed) {
      users[element.userId] = (users[element.userId] || 0) + 1;
    }
  });

  console.log(users);
});
