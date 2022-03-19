function invertBinaryTree(tree) {
  if (tree === null) return;
  let tmp;

  tmp = tree.left;
  tree.left = tree.right;
  tree.right = tmp;
  invertBinaryTree(tree.left);
  invertBinaryTree(tree.right);
  return tree;
}

// This is the class of the input binary tree.
class BinaryTree {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Do not edit the line below.
exports.invertBinaryTree = invertBinaryTree;
