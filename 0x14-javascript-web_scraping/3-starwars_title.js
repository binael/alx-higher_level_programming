#!/usr/bin/node

const urlPath = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

request.get(urlPath, (error, response, body) => {
  if (error) {
    console.log('');
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
