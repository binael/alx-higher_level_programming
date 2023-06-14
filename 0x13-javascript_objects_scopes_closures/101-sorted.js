#!/usr/bin/node
const dict = require('./101-data').dict;

const keys = Object.entries(dict);
const value = Object.values(dict);
const uniqueList = [...new Set(value)];
const newDict = {};
for (const i in uniqueList) {
  const newList = [];
  for (const j in keys) {
    if (keys[j][1] === uniqueList[i]) {
      newList.unshift(keys[j][0]);
    }
  }
  newDict[uniqueList[i]] = newList;
}
console.log(newDict);
