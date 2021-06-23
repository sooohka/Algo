const fs = require('fs')
const readline = require('readline')
function getInput() {
  //   const input = fs
  //     // .readFileSync('/Users/sookang/Desktop/Algorithm/src/javascript/inputs')
  //     .readFileSync('/dev/stdin')
  //     .toString()
  //     .split('\n')
  //   const initStr = input[0]
  //   const operation = input.slice(2).map((v) => v.split(' '))

  //   return { initStr, operation }

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  })

  let initStr
  let count
  let operation = []

  rl.on('line', function (line) {
    if (!initStr) initStr = line
    else if (count === undefined) count = parseInt(line)
    else if (count) {
      operation.push(line.split(' '))
      count--
      if (count === 0) rl.close()
    }
  })

  rl.on('close', function () {
    solution(initStr, operation)
  })
}

getInput()

class Node {
  constructor(data) {
    this.data = data
    this.next = null
    this.prev = null
  }
}

class LinkedList {
  constructor(data) {
    this.front = false
    const strs = data.split('')
    for (let i = 0; i < strs.length; i += 1) {
      if (!this.head) {
        this.head = new Node(strs[i])
        this.cursor = this.head
      } else {
        const newNode = new Node(strs[i])
        newNode.prev = this.cursor
        this.cursor.next = newNode
        this.cursor = newNode
      }
    }
  }
  //커서 왼쪽으로 한칸옮김
  L() {
    if (!this.head) return
    if (this.cursor === this.head) {
      this.front = true
    } else {
      this.cursor = this.cursor.prev
    }
  }
  //커서 오른쪽으로 한칸 옮김
  D() {
    if (!this.head) return
    if (this.cursor.next) {
      this.cursor = this.cursor.next
    }
    this.front = false
  }
  //커서 왼쪽 삭제
  B() {
    if (!this.head) return
    //제일 앞이 아니면면
    if (!this.front) {
      if (this.cursor.prev) {
        const prevNode = this.cursor.prev
        prevNode.next = this.cursor.next
        this.cursor = this.cursor.prev
      } else {
        this.head = this.cursor.next
        this.cursor = this.head
        this.front = true
      }
    }
  }
  //커서 왼쪽에 추가
  P(data) {
    const newNode = new Node(data)
    if (!this.head) {
      this.head = newNode
      this.cursor = this.head
    } else if (this.front) {
      newNode.next = this.cursor
      this.cursor.prev = newNode
      this.head = this.cursor.prev
      this.cursor = this.head
    }
    //다음 노드가 있으면
    else if (this.cursor.next) {
      const nextNode = this.cursor.next
      newNode.next = nextNode
      newNode.prev = this.cursor
      this.cursor.next = newNode
      this.cursor = this.cursor.next
    } else {
      newNode.prev = this.cursor
      this.cursor.next = newNode
      this.cursor = this.cursor.next
    }
  }
  show() {
    let cursor = this.head
    let strs = ''
    while (cursor) {
      strs += cursor.data
      cursor = cursor.next
    }
    console.log(strs)
  }
}
function solution(initStr, operation) {
  //   const { initStr, operation } = getInput()
  const ll = new LinkedList(initStr)
  for (let i = 0; i < operation.length; i += 1) {
    switch (operation[i][0]) {
      case 'L':
        ll.L()
        break
      case 'D':
        ll.D()
        break
      case 'B':
        ll.B()
        break
      case 'P':
        ll.P(operation[i][1])
        break
      default:
        break
    }
    // ll.show()
  }
  ll.show()
}
// solution()
