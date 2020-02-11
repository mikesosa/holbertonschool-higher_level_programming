#!/usr/bin/node
const request = require('request');
const fake = process.argv[2];
request(fake, function (error, response, body) {
  const charId = /18/;
  let count = 0;
  if (error) {
    console.log(error);
  } else {
    const val = JSON.parse(body);
    // console.log(val);
    const results = val.results;
    // console.log(results);
    for (const i of results) {
      // console.log(i);
      const listCharacters = i.characters;
      //  console.log(listCharacters);
      for (const j in listCharacters) {
        // console.log(listCharacters[j]);
        if (charId.test(listCharacters[j]) === true) {
          count++;
        }
      }
    }
  }
  console.log(count);
});

// const request = require('request');
// const preUrl = process.argv[2];
// const url = preUrl.substring( preUrl.length -5 , 0) + "people/18";
// request(url, function (error, response, body) {
//   if (error) {
//     console.error('error:', error);
//   } else {
//     console.log(JSON.parse(body).films.length);
//   }
// });
