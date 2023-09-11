#!/usr/bin/node
const Num = parseInt(process.argv[2]);
if (!isNaN(Num)) {
  console.log('My number: ' + Num);
} else {
  console.log('Not a number');
}
