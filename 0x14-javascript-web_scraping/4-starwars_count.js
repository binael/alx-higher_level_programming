#!/usr/bin/node

const urlPath = process.argv[2];
const request = require('request');
const id = '' + 18;

request.get(urlPath, (error, response, body) => {
  if (error) {
    console.log('');
  } else {
    const data = JSON.parse(body);
    let numOfOccurence = 0;
    for (const result of data.results) {
      for (const character of result.characters) {
        if (character.slice(-3, -1) === id) {
          numOfOccurence += 1;
          break;
        }
      }
    }
    console.log(numOfOccurence);
  }
});
