const fs = require("fs");

// const input = fs
//     .readFileSync("../inputs")
//     .toString()
//     .split("\n")
//     .map((v) => parseInt(v));

const input = fs
.readFileSync("/dev/stdin")
.toString()
.split("\n")
.map((v) => parseInt(v));

let val = 0;
let temp = input[0];
let ans = temp;
while (temp > 0) {
    val = temp;
    let tempo = temp;
    while (tempo > 0) {
        val += Math.floor(tempo % 10);
        tempo /= 10;
    }
    if (val === input[0]) if (ans > temp) ans = temp;
    temp--;
}
if (ans === input[0]) console.log(0);
else console.log(ans);
