const fs = require("fs");

//const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const input = fs.readFileSync("/Users/sooho/Desktop/Algorithms/src/javascript/readme", "utf-8").toString().split("\n");

//n보다 크고 2n보다 작거나 같은 소수 구하기
const pushInput = (arr) => {
    const copied = [];
    for (const i of arr) {
        if (i === "0") return copied;
        copied.push(parseInt(i));
    }
};
const arr = pushInput(input);
const getPrime = (n) => {
    let count = 0;

    if (n == 1 || n == 2) return 1;
    const arr = [false, false];

    for (i = 2; i <= 2 * n; i++) arr.push(true);

    for (i = 2; i <= 2 * n; i++) {
        if (!arr[i]) continue;
        if (arr[i]) for (j = i + i; j <= 2 * n; j += i) arr[j] = false;
    }
    for (i = n + 1; i <= 2 * n; i++) if (arr[i]) count++;
    return count;
};

const printCount = (arr) => {
    arr.forEach((element) => {
        console.log(getPrime(element));
    });
};

printCount(arr);
