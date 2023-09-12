#!/usr/bin/node

const args = process.argv;
const fs = require('fs');
const fileA = fs.readFileSync(args[2], 'utf8');
const fileB = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], fileA + fileB);
