#!/usr/bin/node
const convert = process.argv[2];
const convertNumber = parseInt(convert);
if (isNaN(convertNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convertNumber}`);
}
