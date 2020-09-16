#!/usr/bin/node
let argsLen = 0;
process.argv.forEach((element) => { argsLen++; });
if (argsLen === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
