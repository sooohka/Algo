class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

function getNumberFromLinkedList(linkedList) {
  let currentNode = linkedList;
  let number = "";
  while (currentNode !== null) {
    const curNum = currentNode.value;
    number = curNum + number;
    currentNode = currentNode.next;
  }
  return Number(number);
}

function sumOfLinkedLists(linkedListOne, linkedListTwo) {
  const num1 = getNumberFromLinkedList(linkedListOne);
  const num2 = getNumberFromLinkedList(linkedListTwo);

  let num = num1 + num2;
  let val = num % 10;
  num = Math.floor(num / 10);

  let node = new LinkedList(val);
  const headPointer = node;
  while (num > 0) {
    val = num % 10;
    num = Math.floor(num / 10);
    const newNode = new LinkedList(val);
    node.next = newNode;
    node = node.next;
  }
  return headPointer;
}
