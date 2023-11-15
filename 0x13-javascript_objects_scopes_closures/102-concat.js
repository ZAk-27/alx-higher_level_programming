#!/usr/bin/node
const fs = require('fs').promises;
const { argv } = require('process');
const file1 = argv[2];
const file2 = argv[3];
const file3 = argv[4];
async function concatTwoFiles () {
  try {
    const dataA = await fs.readFile(file1);
    const dataB = await fs.readFile(file2);
    fs.writeFile(file3, dataA + dataB);
  } catch (err) {
    console.log(err);
  }
}
concatTwoFiles();
