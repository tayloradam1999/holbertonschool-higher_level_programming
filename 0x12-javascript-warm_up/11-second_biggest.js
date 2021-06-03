#!/usr/bin/node
const myArgs = process.argv.slice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log('%i', 0);
} else {
  for (let x = 0; x < myArgs.length; x++) {
    if (myArgs[x] > x) {
      x = myArgs[x];
    }
  }
  console.log(x);
}
