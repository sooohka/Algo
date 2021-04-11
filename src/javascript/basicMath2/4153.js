const fs = require("fs");
const input = fs
    .readFileSync("/dev/stdin")
    .toString()
    .split("\n")
    .map((v) => v.split(" ").map((k) => parseInt(k)));
// const input = fs
//     .readFileSync("../inputs")
//     .toString()
//     .split("\n")
//    .map((v) => v.split(" ").map((k) => parseInt(k)));

const my_pow = (v) => {
    return Math.pow(v, 2);
};

const isCorrect = (arr) => {
    arr.sort((a, b) => a - b);
    return my_pow(arr[0]) + my_pow(arr[1]) == my_pow(arr[2]) ? "right" : "wrong";
};

for (i of input) {
    if (i[0] === 0 && i[1] === 0 && i[2] === 0) break;
    console.log(isCorrect(i));
}
