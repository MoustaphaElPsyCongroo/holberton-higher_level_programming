#!/usr/bin/node
const { argv } = process;
const size = parseInt(argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      if (j === size - 1) console.log('X');
      else process.stdout.write('X');
    }
  }
}
