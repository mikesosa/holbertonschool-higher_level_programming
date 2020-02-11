#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const data = JSON.parse(body);
    const arr = [];
    const counts = {};
    Object.keys(data).forEach(function (key) {
      const value = data[key];
      if (value.userId && value.completed) {
        arr.push(value.userId);
      }
    });

    for (let i = 0; i < arr.length; i++) {
      const num = arr[i];
      counts[num] = counts[num] ? counts[num] + 1 : 1;
    }
    console.log(counts);
  }
});
