#!/usr/bin/node
const Args = process.argv.slice(2);
if (isNaN(Args[0])) {
  console.log('Not a number');
} else {
  console.log('My number: %i', Args[0]);
}
