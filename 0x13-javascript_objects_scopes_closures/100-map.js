#!/usr/bin/node
let temp = require('./100-data');
temp = temp.list;
console.log(temp);
console.log(temp.map((index, number) => index * number));
