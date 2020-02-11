#!/usr/bin/node

const fs = require('fs');
const data = process.argv[3];
// Write data in 'Output.txt' .
fs.writeFile(process.argv[2], data, 'utf-8', (err) => {
  // In case of a error throw err.
  if (err) console.log(err);
});
