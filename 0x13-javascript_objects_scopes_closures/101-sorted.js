#!/usr/bin/node

const data = require('./101-data');

const dictByOccurrence = {};

for (const userId in data.dict) {
  const occurrence = data.dict[userId];

  if (!dictByOccurrence[occurrence]) {
    dictByOccurrence[occurrence] = [];
  }

  dictByOccurrence[occurrence].push(userId);
}

console.log(dictByOccurrence);
