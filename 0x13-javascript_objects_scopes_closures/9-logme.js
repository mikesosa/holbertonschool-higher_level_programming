#!/usr/bin/node

let printedLines = 0;

exports.logMe = function (item) {
  console.log(`${printedLines}: ${item}`);
  printedLines++;
};
