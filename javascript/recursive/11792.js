const fs = require("fs");

const input = fs.readFileSync(".../inputs").toString().split("\n");
//const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let str = "";
let count = 0;
const move = (start, end) => {
    str = str.concat("\n" + start + " " + end);
};

const hanoi = (n, from, middle, to) => {
    if (n == 1) {
        move(from, to);
        count++;
        return;
    }
    hanoi(n - 1, from, to, middle);
    hanoi(1, from, middle, to);
    hanoi(n - 1, middle, from, to);
};

const solution = (n) => {
    hanoi(n, 1, 2, 3);
    console.log(count, str);
};

solution(parseInt(input));
