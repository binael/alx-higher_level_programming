#!/usr/bin/node

function add (a, b) {
  const result = Number(a) + Number(b);
  console.log(result);
}

add(process.argv[2], process.argv[3]);
