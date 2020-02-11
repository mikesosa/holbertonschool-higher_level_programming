#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const data = body;
    fs.writeFile(process.argv[3], data, 'utf-8', (err) => {
    // In case of a error throw err.
      if (err) console.log(err);
    });
  }
});
