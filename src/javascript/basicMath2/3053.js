const fs = require("fs");
// const input = fs.readFileSync("../inputs").toString().split("\n");

const input = fs.readFileSync("/dev/stdin").toString().split('\n');

const r = parseInt(input[0]);

console.log((Math.pow(r, 2) * Math.PI).toFixed(6));
console.log((Math.pow(r, 2) * 2).toFixed(6));
