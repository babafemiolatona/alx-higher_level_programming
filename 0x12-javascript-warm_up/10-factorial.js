#!/usr/bin/node
const args = process.argv;
const n = args[2];

function factorial (n) {
  if ((n === 0) || (isNaN(n))) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(n));
