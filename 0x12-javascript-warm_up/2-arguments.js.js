#!/usr/bin/node
// console.log(typeof(process.argv[0]))
// console.log(process.argv[1])
// console.log(process.argv[2])

if (process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
