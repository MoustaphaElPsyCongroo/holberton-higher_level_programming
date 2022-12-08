#!/usr/bin/node
const { argv } = process;
const num = parseInt(argv[2]);

console.log(!isNaN(num) ? `My number: ${num}` : 'Not a number');
