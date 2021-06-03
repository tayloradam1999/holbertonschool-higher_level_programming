#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0])) {
  console.log('%i', 1);
} else {
  console.log(factorial(myArgs[0]));
}

function factorial (x) {
  return (x !== 1) ? x * factorial(x - 1) : 1;
}
