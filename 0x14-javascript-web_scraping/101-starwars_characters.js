#!/usr/bin/node

const urlPath = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');
const util = require('util');
const promiseRequest = util.promisify(request.get);

async function orderedRequest (myUrl) {
  const response = await promiseRequest(myUrl);
  const person = JSON.parse(response.body);
  console.log(person.name);
}

request.get(urlPath, async (error, response, body) => {
  if (error) {
    console.log('');
  } else {
    const data = JSON.parse(body);
    for (const urlPerson of data.characters) {
      await orderedRequest(urlPerson);
    }
  }
});
