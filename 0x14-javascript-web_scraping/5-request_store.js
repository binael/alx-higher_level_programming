#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const urlPath = process.argv[2];
const filePath = process.argv[3];

request
  .get(urlPath)
  .pipe(fs.createWriteStream(filePath, { encoding: 'utf-8' }));
