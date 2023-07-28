#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request.get(urlPath, (error, response, body) => {
  if (error) {
    console.log('');
  } else {
    const data = JSON.parse(body);
    const objFile = {};

    data.forEach((user) => {
      if (user.completed) {
        const userId = user.userId;
        objFile[userId] = (objFile[userId] || 0) + 1;
      }
    });
    console.log(objFile);
  }
});
