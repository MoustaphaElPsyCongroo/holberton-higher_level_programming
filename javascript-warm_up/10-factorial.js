#!/usr/bin/node
const { argv } = process;
const n = parseInt(argv[2]) || 1;

function factorial (n) {
  if (n < 0) return -1;
  if (n === 0) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(n));
