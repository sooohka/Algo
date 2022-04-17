// This is an input class. Do not edit.
class BST {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function validateBst(tree) {
  return f(tree, -Infinity, Infinity)
}

function f(tree, min, max) {
  if (tree === null) return true
  if (tree.value < min) return false
  if (tree.value >= max) return false
  return f(tree.left, min, tree.value) && f(tree.right, tree.value, max)
}

// Do not edit the line below.
exports.BST = BST
exports.validateBst = validateBst

// 이진탐색트리인지 검사하는 문제
// 1. 이진탐색트리의 왼쪽에 들어오는 값은 항상 부모보다 작아야함
// 2. 이진탐색트리의 오른쪽에 들어오는 값은 항상 부모보다 크거나 같아야함
// 3. 이진탐색트리의 자식은 항상 부모의 최소값보다 크거나 같고 최댓값보다 작아야함
//
// 자식의 최소, 최댓값을 구해서 재귀함수로 전달해주고 리프노드까지 오면 true
// 실패조건에 걸리면 false 리턴함
