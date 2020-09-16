#!/usr/bin/node
let convert = process.argv[2];
convert = parseInt(x);
if (isNaN(convert)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < convert; i++) {
    console.log('C is fun');
  }
}
