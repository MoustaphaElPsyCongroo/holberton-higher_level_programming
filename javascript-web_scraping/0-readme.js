#!/usr/bin/node
const { readFile } = require('fs/promises');
const { argv } = process;

const path = argv[2];

(async function (path) {
  try {
    const data = await readFile(path, 'utf8');
    console.log(data);
  } catch (error) {
    console.log(error);
  }
})(path);
