#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (isNaN(myArgs[0]) || isNaN(myArgs[1])) {
  console.log('NaN');
} else {
  console.log(add(myArgs[0], myArgs[1]));
}

function add (a, b) {
  return +a + +b;
}
