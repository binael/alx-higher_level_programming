#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const arr = process.argv.slice(2);
  let secondElement = Number.MIN_VALUE;
  let maxValue = Number.MIN_VALUE;

  arr.forEach(function (element) {
    element = parseInt(element);
    if (element > maxValue) {
      secondElement = maxValue;
      maxValue = element;
    } else if (element > secondElement) {
      secondElement = element;
    }
  });
  console.log(secondElement);
}
