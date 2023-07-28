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
	const entries = Object.entries(objFile);
	let index = 0;
	while (index < entries.length) {
		const [key, value] = entries[index];

		if (index == 0) {
			console.log(`{ '${key}': ${value}, `);
		} else if (index == entries.length - 1) {
			console.log(`  '${key}': ${value} }`)
		} else {
			console.log(`  '${key}': ${value}, `)
		}
		index++;
	}
  }
});
