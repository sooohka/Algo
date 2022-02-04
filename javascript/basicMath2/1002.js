const fs = require("fs");

const input = fs
    .readFileSync("../inputs")
    .toString()
    .split("\n")
    .map((v) => v.split(" ").map((k) => parseInt(k)));
// const input=fs.readFileSync("/dev/stdin").toString().split('\n').map((v)=>v.split(' ').map((k)=>parseInt(k)))

//1. 두원이 같을때 -1
//2. 두원이 좌표는 같지만 반지름이 다를떄 0
//3. 두원의 거리가 반지름합의 거리보다 클때 0
//4. 두원의 거리와 반지름의 합이 같을때 1
//5. 두원의 거리가 반지름의 합이 거리보다 짧을때 2
//6.
const turret = (x1, y1, r1, x2, y2, r2) => {
    let sumr = r2 + r1;
    let sumxy = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    if (x1 === x2 && y1 === y2) {
        if (r1 === r2) return -1;
        return 0;
    } 
    else if (Math.abs(r2 - r1) > sumxy) return 0;
    else if (Math.abs(r2 - r1) === sumxy) return 1;
    else if (sumr === sumxy) return 1;
    else if (sumxy > sumr) return 0;
    else return 2;
};

const solution = (input) => {
    let x1, y1, r1, x2, y2, r2;

    for (let i = 1; i <= input[0]; i++) {
        x1 = input[i][0];
        y1 = input[i][1];
        r1 = input[i][2];
        x2 = input[i][3];
        y2 = input[i][4];
        r2 = input[i][5];
        console.log(turret(x1, y1, r1, x2, y2, r2));
    }
};

solution(input);
