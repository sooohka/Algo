const fs = require("fs");
// const input = fs
//     .readFileSync("../inputs")
//     .toString()
//     .split("\n")
//     .map((v) => v.split(" ").map((k) => parseInt(k)));
const input = fs
    .readFileSync("/dev/stdin")
    .toString()
    .split("\n")
    .map((v) => v.split(" ").map((k) => parseInt(k)));

const N = input[0][0];
const M = input[0][1];
const cards = input[1];

let sum = 0;
for (i of cards) {
    for (j of cards) {
        if (i === j) continue;
        for (k of cards) {
            if ( j=== k||k === i) continue;
            if (i + j + k > sum && i + j + k <= M) {
                sum = i + j + k;
            }
        }
    }
}
console.log(sum);
