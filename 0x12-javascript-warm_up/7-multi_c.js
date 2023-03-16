#!/usr/bin/node
const nb = Math.floor(Number(process.argv[2]));
if (isNaN(nb)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < nb; i++) {
    console.log('C is fun');
  }
}
