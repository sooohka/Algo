// This is an input class. Do not edit.
class AncestralTree {
  constructor(name) {
    this.name = name;
    this.ancestor = null;
  }
}

function getHeight(tree) {
  let h = 1;
  while (tree !== null) {
    h += 1;
    tree = tree.ancestor;
  }
  return h;
}

function getCommon(younger, older, youngerHeight, olderHeight) {
  /* 높이를 먼저 맞추고 */
  while (youngerHeight > olderHeight) {
    youngerHeight -= 1;
    younger = younger.ancestor;
  }
  /* 공통부모 찾는다 */
  while (younger !== older) {
    younger = younger.ancestor;
    older = older.ancestor;
  }
  return younger;
}

function getYoungestCommonAncestor(topAncestor, one, two) {
  const oneHeight = getHeight(one);
  const twoHeight = getHeight(two);
  if (oneHeight > twoHeight) {
    return getCommon(one, two, oneHeight, twoHeight);
  }
  return getCommon(two, one, twoHeight, oneHeight);
}
