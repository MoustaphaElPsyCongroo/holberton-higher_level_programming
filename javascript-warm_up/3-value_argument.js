#!/usr/bin/node
const { argv } = process;

if (argv.length < 3) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
