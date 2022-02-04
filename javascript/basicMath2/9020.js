const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().split("\n");
//const input = fs.readFileSync("../inputs", "utf-8").toString().split("\n");

const getAns = (inputs) => {
    const arr = [];
    inputs.forEach((element) => arr.push(parseInt(element)));
    for (let i = 1; i <= arr[0]; i++) {
        printGoldBahu(arr[i]);
    }
};

const getPrimes = (n) => {
    const arr = [false, false];
    const primes = [];
    for (let i = 2; i < n; i++) arr.push(true);
    for (let i = 2; i < n; i++) {
        if (!arr[i]) continue;
        if (arr[i]) for (j = i + i; j < n; j += i) arr[j] = false;
    }
    arr.forEach((v, i) => {
        if (v) primes.push(i);
    });
    return primes;
};

const printGoldBahu = (n) => {
    const primes = getPrimes(n);
    let val = [0, n];
    for (let i = 0; i < primes.length; i++) {
        for (j = primes.length - 1; j >= i; j--) {
            if (primes[i] + primes[j] < n) break;
            if (primes[i] + primes[j] === n) {
                if (val[1] - val[0] > primes[j] - primes[i]) {
                    val[1] = primes[j];
                    val[0] = primes[i];
                }
            }
        }
    }
    console.log(val.join(' '));
};

getAns(input);
