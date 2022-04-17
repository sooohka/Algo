// Do not edit the class below except
// for the breadthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
  constructor(name) {
    this.name = name
    this.children = []
  }

  addChild(name) {
    this.children.push(new Node(name))
    return this
  }

  breadthFirstSearch(array) {
    const stack = [this]
    while (stack.length !== 0) {
      const cur = stack.shift()
      for (const child of cur.children) {
        stack.push(child)
      }
      array.push(cur.name)
    }
    return array
  }
}

// Do not edit the line below.
exports.Node = Node
