#!/usr/bin/node
const argsList = process.argv.slice(2).map(num => parseInt(num));
const sortedList = argsList.sort((a, b) => a < b);
if (sortedList.length <= 1) {
  console.log(0);
} else {
  console.log(sortedList[1]);
}
