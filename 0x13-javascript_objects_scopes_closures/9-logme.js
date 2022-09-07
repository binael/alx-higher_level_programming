#!/usr/bin/node

let num = -1;
exports.logMe = function (item) {
  function printLog (item) {
    num++;
    console.log(`${num}: ${item}`);
  }
  return printLog(item);
};
