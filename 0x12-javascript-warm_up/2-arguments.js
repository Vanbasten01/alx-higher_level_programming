#!/usr/bin/node
const numofargs = process.argv.length;
if (numofargs === 2) {
  console.log('No argument');
} else if (numofargs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
