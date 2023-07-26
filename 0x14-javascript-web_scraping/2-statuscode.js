#!/usr/bin/node

const urlPath = process.argv[2];
const request = require('request');

request.get(urlPath).on('response', (response) => {
  console.log(`code: ${response.statusCode}`);
});
