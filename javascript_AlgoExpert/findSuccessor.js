//
// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
    this.parent = null;
  }
}

//O(n)time O(n) space
function inOrder(tree, arr) {
  if (tree === null) {
    return null;
  }

  inOrder(tree.left, arr);
  arr.push(tree);
  inOrder(tree.right, arr);
  return arr;
}

function findSuccessor(tree, node) {
  let ans;
  const arr = inOrder(tree, []);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].value === node.value) {
      if (arr[i + 1]) ans = arr[i + 1];
      break;
    }
  }
  if (ans === undefined) ans = null;
  return ans;
}
// O(h)time O(1)space
function findSuccessor(tree, node) {
  if (node.right !== null) {
    let cur = node.right;
    while (cur.left !== null) {
      cur = cur.left;
    }
    return cur;
  }
  if (node.parent !== null) {
    if (node.parent.left === node) {
      return node.parent;
    }
    if (node.parent.right === node) {
      return node.parent.parent;
    }
  }
  return null;
}
/*
중위순회이기 때문에 왼쪽 -> 중간 -> 오른쪽 노드 순으로 탐색하게 된다.

1.현재 노드에 오른쪽 자식이 있는 경우
	1-1. 오른쪽 자식에 왼쪽 자식이 있는 경우
		오른쪽 자식의 제일 왼쪽자식이 successor가 된다.
	1-2. 오른쪽 자식에 왼쪽 자식이 없는 경우
		오른쪽 자식이 successor가 된다.
		
2. 그 외
	1-1.현재 노드가 부모의 왼쪽에 있는 경우
		현재 노드의 부모가 successor가 된다.
	1-2.현재 노드가 부모의 오른쪽에 있는 경우
		현재 노드의 부모의 부모가 successor가 된다.
*/
