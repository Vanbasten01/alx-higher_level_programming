#!/usr/bin/node
const numofoccu = parseInt(process.argv[2]);
if (!isNaN(numofoccu)) {
  for (let i = 0; i < numofoccu; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
