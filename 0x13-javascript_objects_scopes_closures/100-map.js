#!/usr/bin/node
const { list } = require('./100-data');
const mapList = list.map((value, index) => {
  return value * index;
});
console.log(list);
console.log(mapList);
