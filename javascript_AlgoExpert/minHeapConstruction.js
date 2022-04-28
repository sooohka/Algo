// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
class MinHeap {
  constructor(array) {
    this.heap = this.buildHeap(array);
  }

  buildHeap(array) {
    this.heap = [];
    array.forEach((v) => {
      this.insert(v);
    });
    return this.heap;
  }

  peek() {
    return this.heap[0];
  }

  /*
   * 1. 제일끝과 루트노드 swap
   * 2. swap된 노드랑 자식노드랑 비교해서 더 작은값이랑 swap
   */
  remove() {
    if (this.heap.length === 0) {
      return undefined;
    }
    if (this.heap.length === 1) {
      return this.heap.pop();
    }
    if (this.heap.length === 2) {
      const v = this.heap[0];
      this.heap = [this.heap[1]];
      return v;
    }
    let temp = this.heap[0];
    this.heap[0] = this.heap[this.heap.length - 1];
    this.heap[this.heap.length - 1] = temp;

    const root = this.heap.pop();

    let currentIdx = 0;
    let smallerIdx = this.heap[1] < this.heap[2] ? 1 : 2;
    while (this.heap[currentIdx] > this.heap[smallerIdx]) {
      temp = this.heap[currentIdx];
      this.heap[currentIdx] = this.heap[smallerIdx];
      this.heap[smallerIdx] = temp;

      currentIdx = smallerIdx;
      if (currentIdx * 2 + 1 >= this.heap.length) {
        break;
      }
      if (currentIdx * 2 + 2 >= this.heap.length) {
        smallerIdx = currentIdx * 2 + 1;
      } else {
        smallerIdx =
          this.heap[currentIdx * 2 + 1] < this.heap[currentIdx * 2 + 2]
            ? currentIdx * 2 + 1
            : currentIdx * 2 + 2;
      }
    }
    return root;
  }

  /*
   * 1. 제일 끝에 push
   * 2. 부모와 비교하면서 부모보다 자신이 작으면 부모랑 swap
   */
  insert(value) {
    if (this.heap.length === 0) {
      this.heap = [value];
      return;
    }
    this.heap.push(value);
    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor((currentIdx - 1) / 2);
    while (this.heap[currentIdx] < this.heap[parentIdx]) {
      const temp = this.heap[currentIdx];
      this.heap[currentIdx] = this.heap[parentIdx];
      this.heap[parentIdx] = temp;
      currentIdx = parentIdx;
      parentIdx = Math.floor((currentIdx - 1) / 2);
    }
  }
}
