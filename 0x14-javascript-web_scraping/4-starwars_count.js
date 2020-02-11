#!/usr/bin/node

const request = require('request');
const preUrl = process.argv[2];
const url = preUrl.substring( preUrl.length -5 , 0) + "people/18";
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
