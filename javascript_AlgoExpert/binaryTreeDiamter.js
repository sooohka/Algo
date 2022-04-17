// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function helper(tree) {
  if (tree === null) return { d: 0, h: 0 }

  const left = helper(tree.left)
  const right = helper(tree.right)

  const currentHeight = Math.max(left.h, right.h) + 1
  const currentDiamter = left.h + right.h
  const longest = Math.max(currentDiamter, left.d, right.d)
  return { h: currentHeight, d: longest }
}

function binaryTreeDiameter(tree) {
  return helper(tree).d
}

// Do not edit the line below.
exports.binaryTreeDiameter = binaryTreeDiameter
exports.BinaryTree = BinaryTree

// 트리 내에서 겹치지 않는 최대경로를 구하는 문제
//
// 현재 노드에서 최대경로가 될 수 있는 후보
// 1. 현재 노드 기준 왼쪽노드의 높이 + 오른쪽 노드의 높이
// 2. 오른쪽 노드의 최대경로
// 3. 왼쪽 노드의 최대경로
//
// 재귀적으로 돌면서 각 노드별로 높이와 최대경로를 구하면 됨
