#!/usr/bin/node
const passedArg = process.argv[2];
const num = parseInt(passedArg);
const n = (function factorial (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else if (num < 0) {
    return 'Factorial of a negative number does not exist';
  } else {
    return (num * factorial(num - 1));
  }
})(num);
console.log(n);
