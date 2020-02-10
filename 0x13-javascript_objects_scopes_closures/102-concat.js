#!/usr/bin/node
const fs = require('fs');
let c = fs.readFileSync(process.argv[2]);
c += fs.readFileSync(process.argv[3]);
fs.writeFile(process.argv[4], c);
