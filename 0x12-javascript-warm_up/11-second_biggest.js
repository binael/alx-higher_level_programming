#!/usr/bin/node

const len = process.argv.length;
if (len < 4) {
  console.log('0');
} else {
  let maxNum = Number(process.argv[2]);
  let secondMax = Number(process.argv[3]);

  for (let i = 3; i < len; i++) {
    if (maxNum < process.argv[i]) {
      secondMax = maxNum;
      maxNum = process.argv[i];
    } else if (secondMax < process.argv[i]) {
      secondMax = process.argv[i];
    }
  }
  console.log(secondMax);
}
