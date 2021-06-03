#!/usr/bin/node
const myArg = process.argv.slice(2);
if (isNaN(myArg[0])) {
  console.log('Missing size');
} else {
  let myStr = '';
  for (let x = 0; x < myArg[0]; x++) {
    myStr += 'X';
  } for (let y = 0; y < myStr.length; y++) {
    console.log(myStr);
  }
}
