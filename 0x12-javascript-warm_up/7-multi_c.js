#!/usr/bin/node

const userArgs = Number(process.argv[2]);
let i = 0;

if (!userArgs) {
  console.log('Missing number of occurrences');
}
else {
  for (i = 0; i < userArgs; i++) {
    console.log('C is fun');
  }
}
