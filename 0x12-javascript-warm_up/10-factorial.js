#!/usr/bin/node

function factorial (num) {
  if (num === 1 || num === 0 || isNaN(num)) {
    return (1);
  }
  return (factorial(num - 1) * num);
}
console.log(factorial(parseInt(process.argv[2])));
