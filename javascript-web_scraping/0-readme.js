#!/usr/bin/node
const { readFile } = require('node:fs');
const { argv } = process;

const path = argv[2];

readFile(path, 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});

// With Promises, but checker doesn't support this version :(
// (async function (path) {
//   try {
//     const data = await readFile(path, 'utf8');
//     console.log(data);
//   } catch (error) {
//     console.log(error);
//   }
// })(path);
