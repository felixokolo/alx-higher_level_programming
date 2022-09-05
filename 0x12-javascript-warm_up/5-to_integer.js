#!/usr/bin/node
let myNumber;
if (process.argv.length === 2) { myNumber = 'Not a number'; } else { myNumber = Number(process.argv.slice(2, 3)); }
if (isNaN(myNumber)) {
  myNumber = 'Not a number';
}
if (myNumber === 'Not a number')
	console.log(myNumber)
else
	console.log('My number: ' + myNumber);
