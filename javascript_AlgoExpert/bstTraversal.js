// 중위순회 left root right
function inOrderTraverse(tree, array) {
  if (tree === null) return;

  inOrderTraverse(tree.left, array);
  array.push(tree.value);
  inOrderTraverse(tree.right, array);
  return array;
}

// 전위순회 root left right
function preOrderTraverse(tree, array) {
  if (tree === null) return;

  array.push(tree.value);
  preOrderTraverse(tree.left, array);
  preOrderTraverse(tree.right, array);
  return array;
}
// 후위순회 left right root
function postOrderTraverse(tree, array) {
  if (tree === null) return;
  postOrderTraverse(tree.left, array);
  postOrderTraverse(tree.right, array);
  array.push(tree.value);
  return array;
}

// Do not edit the lines below.
exports.inOrderTraverse = inOrderTraverse;
exports.preOrderTraverse = preOrderTraverse;
exports.postOrderTraverse = postOrderTraverse;
