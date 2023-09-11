#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  let grid = '';
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      grid += 'X';
    }
    console.log(grid);
    grid = '';
  }
} else {
  console.log('Missing size');
}
