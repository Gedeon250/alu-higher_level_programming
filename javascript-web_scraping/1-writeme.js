#!/usr/bin/node
const fs = require('fs');
const Path = process.argv[2];
const content = process.argv[3];
fs.writeFile(Path, content, 'utf-8', (error, content) => {
  if (error) { console.log(error); }
});
