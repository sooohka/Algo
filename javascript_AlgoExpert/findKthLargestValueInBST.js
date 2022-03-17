// This is an input class. Do not edit.
class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}
// 오른쪽 -> 중간 -> 왼쪽 순으로 k번 순회
function RMLTraverse(array, tree) {
  if (tree === null) return;
  RMLTraverse(array, tree.right);
  array.push(tree.value);
  RMLTraverse(array, tree.left);
}
function findKthLargestValueInBst(tree, k) {
  const array = [];
  RMLTraverse(array, tree);
  return array[k - 1];
}

//k번째로 큰 값을 이진탐색트리에서 찾기
//오른족 -> 중간 -> 왼쪽순으로 tree를 k번 순회하면 됨
//오른쪽 -> 중간 -> 왼쪽순으로 트리를 순회하는 함수를 작성하면 끝

// Do not edit the lines below.
exports.BST = BST;
exports.findKthLargestValueInBst = findKthLargestValueInBst;
