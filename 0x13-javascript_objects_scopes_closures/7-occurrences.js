#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let number = 0;
  for (const i of list) {
    if (i === searchElement) {
      number += 1;
    }
  }

  return (number);
};
