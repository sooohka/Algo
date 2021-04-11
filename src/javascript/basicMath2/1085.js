const fs = require("fs");

//const input = fs.readFileSync("../inputs").toString().split(" ");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

const arr = [];
for (i of input) arr.push(parseInt(i));
const hansu = [arr[0], arr[1]];
const rightTop = [arr[2], arr[3]];
const getClosest = (hansu, rightTop) => {
    let x = 0;
    let y = 0;
    x = hansu[0] > rightTop[0] - hansu[0] ? rightTop[0] - hansu[0] : hansu[0];
    y = hansu[1] > rightTop[1] - hansu[1] ? rightTop[1] - hansu[1] : hansu[1];
    return x > y ? y : x;
};
console.log(getClosest(hansu, rightTop));
