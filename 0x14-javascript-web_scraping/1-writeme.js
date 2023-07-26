#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const text = process.argv[3] + '\n';

fs.writeFile(filePath, text, {encoding: 'utf-8'}, (err) => {
  if (err) {
    console.error(err);
  }
});
