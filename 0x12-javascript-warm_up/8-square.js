#!/usr/bin/node

const squareSize = Number(process.argv[2]);
let row = '';

if (process.argv.length < 3 || !squareSize) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    for (let j = 0; j < squareSize; j++) {
      row += 'X';
    }
    console.log(row);
    row = '';
  }
}
