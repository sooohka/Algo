const fs = require("fs");

//const input=fs.readFileSync("/dev/stdin").toString().split('\n').map((v)=>parseInt(v.split(' ')))
const input = fs
    .readFileSync("../inputs")
    .toString()
    .split("\n")
    .map((v) => v.split(" "));

const getCoord = (coords) => {
    const x = [];
    const y = [];
    let ans = [];
    for (let i in coords) {
        x.push(coords[i][0]);
        y.push(coords[i][1]);
    }
    if (x[0] === x[1]) ans[0] = x[2];
    else ans[0] = x[0] === x[2] ? x[1] : x[0];
    if (y[0] === y[1]) ans[1] = y[2];
    else ans[1] = y[0] === y[2] ? y[1] : y[0];
    console.log(ans.join(" "));
};
getCoord(input);
