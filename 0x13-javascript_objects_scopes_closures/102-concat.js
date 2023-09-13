#!/usr/bin/node
const fs = require('fs');
const args = process.argv;
const a = fs.readFileSync(args[2], 'utf-8');
const b = fs.readFileSync(args[3], 'utf-8');
fs.writeFileSync(args[4], a + b);
