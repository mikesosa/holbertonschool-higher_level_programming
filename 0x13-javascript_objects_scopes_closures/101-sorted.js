#!/usr/bin/node
let temp = require('./101-data');
temp = temp.dict;
const MYDICT = {};
for (const key in temp) {
  // MYDICT[temp[i]].push(temp[i]);
  // TypeError: Cannot read property 'push' of undefined FUUUU
  if (MYDICT[temp[key]] === undefined) {
    MYDICT[temp[key]] = [];
  }
  MYDICT[temp[key]].push(key);
}
console.log(MYDICT);
