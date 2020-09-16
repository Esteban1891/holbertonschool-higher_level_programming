#!/usr/bin/node
if (3 <= process.argv.length) {
    console.log(process.argv[2]);
} else {
  console.log('No argument');
}
