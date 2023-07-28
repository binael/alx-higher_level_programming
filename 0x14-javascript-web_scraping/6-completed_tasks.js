#!/usr/bin/node

const request = require('request');
const urlPath = process.argv[2];

request.get(urlPath, (error, response, body) => {
  if (error) {
    console.log('');
  } else {
    const data = JSON.parse(body);
    const objFile = {};

    for (const user of data) {
      const id = '' + user.userId;
      if (!objFile[id]) {
        objFile[id] = 0;
      }
      if (user.completed === true) {
        objFile[id] += 1;
      }
    }
    const newObj = JSON.stringify(objFile);
    console.log(newObj);
  }
});
