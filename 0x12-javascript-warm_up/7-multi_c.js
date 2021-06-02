#!/usr/bin/node
const myArg = process.argv.slice(2);
if (isNaN(myArg[0])) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < myArg[0]; x++) {
    console.log('C is fun');
  }
}
