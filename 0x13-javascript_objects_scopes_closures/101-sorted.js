#!/usr/bin/node
const dict = require('./101-data').dict;
const nvDict = {};
for (const k in dict) {
  if (nvDict[dict[k]] === undefined) {
    nvDict[dict[k]] = [];
  }
  nvDict[dict[k]].push(k);
}
console.log(nvDict);
