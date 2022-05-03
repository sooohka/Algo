// Feel free to add new properties and methods to the class.
class MinMaxStack {
  constructor() {
    this.min = [];
    this.max = [];
    this.stack = [];
  }

  peek() {
    if (this.stack.length === 0) return undefined;
    return this.stack[this.stack.length - 1];
  }

  pop() {
    if (this.stack.length === 0) return undefined;
    this.min.pop();
    this.max.pop();
    return this.stack.pop();
  }

  push(number) {
    if (this.stack.length === 0) {
      this.min.push(number);
      this.max.push(number);
      this.stack.push(number);
      return;
    }
    if (number > this.max[this.max.length - 1]) {
      this.max.push(number);
      this.min.push(this.min[this.min.length - 1]);
      this.stack.push(number);
      return;
    }
    if (number < this.min[this.min.length - 1]) {
      this.min.push(number);
      this.max.push(this.max[this.max.length - 1]);
      this.stack.push(number);
      return;
    }
    this.min.push(this.min[this.min.length - 1]);
    this.max.push(this.max[this.max.length - 1]);
    this.stack.push(number);
  }

  getMin() {
    return this.min[this.min.length - 1];
  }

  getMax() {
    return this.max[this.max.length - 1];
  }
}
