#!/usr/bin/node
exports.addMeMaybe = (number, theFunction) => {
  number += 1;
  theFunction(number);
};
