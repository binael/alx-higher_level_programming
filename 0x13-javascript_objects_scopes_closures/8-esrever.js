#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length;
  const newList = [];
  let index = 0;

  for (let i = len - 1; i >= 0; i--) {
    newList[index] = list[i];
    index++;
  }
  return (newList);
};
