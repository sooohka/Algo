// This is an input class. Do not edit.
class BST {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }
}

function reconstructBst(array) {
  if (array.length === 0) return null;
  let root = new BST(array[0]);
  let idx = array.length;
  for (let i = 1; i < array.length; i += 1) {
    if (array[i] >= root.value) {
      idx = i;
      break;
    }
  }
  root.left = reconstructBst(array.slice(1, idx));
  root.right = reconstructBst(array.slice(idx, array.length));
  return root;
}

// 전위 탐색으로 찾은 값들을 가지고 이진탐색트리를 만드는 문제
// 기준점을 잡고 기준점까지 재귀함수를 돌며 값을 넣어주면 됨
// 각각의 자식노드를 하나의 트리로 보아 각 자식노드별로 재귀함수를 돌려줄거임(자식트리라고 하겠음)
// 이때 자식트리(배열)의 루트노드의 값보다 커지는 값이 있는데 이 값은 자식트리의 오른쪽 값으로 들어감.
// 자식트리의 오른쪽 값으로 들어갈 idx를 구해주고 root.left에 자식트리의 배열을
// 매개변수로 하는 재귀함수를 돌릴건데 이때 매개변수로 들어가는 배열은 idx까지 값을 짤라서 넣어주고
// root.right에 들어가는 배열에는 idx부터 배열의 길이까지 짤라서 넣어줌

// Do not edit the lines below.
exports.BST = BST;
exports.reconstructBst = reconstructBst;
