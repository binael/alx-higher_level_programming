#!/usr/bin/node

const inputSize = Number(process.argv[2]);
let squareIndicator = '';

if (process.argv.length < 3 || !inputSize) {
  console.log('Missing size');
} else {
  for (let i = 0; i < inputSize; i++) {
    for (let j = 0; j < inputSize; j++) {
      squareIndicator += 'X';
    }
    console.log(squareIndicator);
    squareIndicator = '';
  }
}
