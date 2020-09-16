#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}

