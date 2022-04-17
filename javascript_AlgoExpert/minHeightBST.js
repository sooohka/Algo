function minHeightBst(array) {
  return bInsert(array, 0, array.length - 1)
}

function bInsert(array, start, end) {
  if (start > end) {
    return null
  }
  const mid = Math.floor((start + end) / 2)
  const bst = new BST(array[mid])
  bst.left = bInsert(array, start, mid - 1)
  bst.right = bInsert(array, mid + 1, end)
  return bst
}

// 최소 높이의 이진탐색트리를 만드는 문제
// 최소 높이의 이진탐색트리를 만드려면 최대한 트리의 균형이 맞아야함
// 트리의 부모로 부터 나온 자식이 항상 even해야함
// 각 노드의 중간값부터 채워넣고 left, right노드를 정하는게 좋을것 같다고 판단함
// 이진탐색 알고리즘을 사용함
// 이진탐색 알고리즘으로 중간값을 넣어주고 재귀적으로 중간
// 값보다 왼쪽, 오른쪽에 대해서도 이진탐색알고리즘을 호출
// 끝점에 맞닿으면 리프노드임으로 null값을 넣어줌
//
// - 처음에는 BST의 insert 메서드를 사용했는데 insert메서드도 내부적으로 트리를 탐색하는
// 불필요한 연산이 있어서 이를 최적화 하기위해 bst를 생성해 bInsert함수에서 바로 값으로 넣어줌

/* 원래 주어진 클래스 */
class BST {
  constructor(value) {
    this.value = value
    this.left = null
    this.right = null
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value)
      } else {
        this.left.insert(value)
      }
    } else if (this.right === null) {
      this.right = new BST(value)
    } else {
      this.right.insert(value)
    }
  }
}

// Do not edit the line below.
exports.minHeightBst = minHeightBst
