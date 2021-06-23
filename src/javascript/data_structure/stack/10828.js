// # push X: 정수 X를 스택에 넣는 연산이다.
// # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// # size: 스택에 들어있는 정수의 개수를 출력한다.
// # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
// # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

const fs = require("fs");

class Stack {
    constructor() {
        this.stack = [];
        this.calls = [];
    }
    push(a) {
        this.stack[this.stack.length] = a;
    }
    pop() {
        if (!this.stack.length) return -1;
        else {
            const temp = this.stack[this.stack.length - 1];
            this.stack = this.stack.filter((v, i, a) => i != this.stack.length - 1);
            return temp;
        }
    }
    size() {
        let count = 0;
        for (let i of this.stack) count += 1;
        return count;
    }
    empty() {
        if (this.stack.length == 0) {
            return 1;
        } else {
            return 0;
        }
    }
    top() {
        if (this.stack.length !== 0) return this.stack[this.stack.length - 1];
        else return -1;
    }
}

const solution = (stack, input) => {
    let str = "";
    for (let i = 1; i < input.length; i++) {
        logic = input[i][0];
        switch (logic) {
            case "push":
                stack.push(parseInt(input[i][1]));
                break;
            case "pop":
                str += stack.pop() + "\n";
                break;
            case "size":
                str += stack.size() + "\n";
                break;
            case "empty":
                str += stack.empty() + "\n";
                break;
            case "top":
                str += stack.top() + "\n";
                break;
        }
    }
    console.log(str);
};

input = fs
    .readFileSync("/dev/stdin") //"../inputs"
    .toString()
    .split("\n")
    .map((v, i) => v.split(" "));
const stack = new Stack();
solution(stack, input);
