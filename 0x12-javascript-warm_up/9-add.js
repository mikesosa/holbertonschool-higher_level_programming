#!/usr/bin/node
function add (a, b) {
  if (!Number(a) || !Number(b)) {
    console.log('NaN');
  } else {
    const a = parseInt(process.argv[2]);
    const b = parseInt(process.argv[3]);
    console.log(a + b);
  }
}

add(process.argv[2], process.argv[3]);
