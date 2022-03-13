class BST {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }

  insert(value) {
    if (value < this.value) {
      if (this.left === null) {
        this.left = new BST(value);
      } else {
        this.left.insert(value);
      }
    } else {
      if (this.right === null) {
        this.right = new BST(value);
      } else {
        this.right.insert(value);
      }
    }
    return this;
  }

  contains(value) {
    if (value === this.value) {
      return true;
    }
    if (value < this.value) {
      if (this.left === null) return false;
      return this.left.contains(value);
    }
    if (this.right === null) return false;
    return this.right.contains(value);
  }

  remove(value, parent = null) {
    if (value < this.value) {
      if (this.left !== null) {
        return this.left.remove(value, this);
      }
    } else if (value > this.value) {
      if (this.right !== null) {
        return this.right.remove(value, this);
      }
    } else {
      let node, temp;
      if (this.right === null && this.left === null) {
        if (parent === null) {
          return;
        } else {
          if (value < parent.value) {
            parent.left = null;
          } else {
            parent.right = null;
          }
        }
        return;
      } else if (this.left === null) {
        node = this.right;
        this.value = node.value;
        this.left = node.left;
        this.right = node.right;
      } else if (this.right === null) {
        node = this.left;
        this.value = node.value;
        this.left = node.left;
        this.right = node.right;
      } else {
        temp = this;
        node = this.right;
        while (node.left !== null) {
          temp = node;
          node = node.left;
        }
        if (temp === this) {
          this.value = node.value;
          this.right = node.right;
        } else {
          this.value = node.value;
          temp.left = node.right;
        }
      }
    }
  }
}

// Do not edit the line below.
exports.BST = BST;
