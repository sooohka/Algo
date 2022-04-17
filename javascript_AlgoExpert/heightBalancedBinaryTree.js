// This is an input class. Do not edit.
class BinaryTree {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }
}

function helper(tree, ans) {
  if (tree === null) {
    return 0
  }
  const leftH = helper(tree.left, ans)
  const rightH = helper(tree.right, ans)
  if (Math.abs(leftH - rightH) > 1) {
    ans.ans = false
  }
  if (leftH > rightH) {
    return leftH + 1
  }
  return rightH + 1
}

function heightBalancedBinaryTree(tree) {
  const ans = { ans: true }
  helper(tree, ans)
  return ans.ans
}
/*
 모든 노드에 대해 왼쪽 자식, 오른쪽 자식의 높이의 차이가 1이하임을 확인하는 문제
재귀함수를 통해 모든 노드를 순회하면서 노드의 왼쪽 자식의 높이, 오른쪽 자식의 높이를 구한 뒤 
이 둘의 높이의 차가 1이하임을 확인한다. 높이의 차이가 1 이하인 경우 높이가 더 높은자식에 + 1해서
현재 노드의 높이를 리턴하고 1초과인 경우 파라미터로 받은 ans값을 변경해준다.
(pass by reference이기 떄문에 오브젝트의 내부 값 변경 가능)
 */
