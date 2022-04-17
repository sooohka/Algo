function riverSizes(matrix) {
  const visited = []
  const ans = []
  for (let i = 0; i < matrix.length; i += 1) {
    visited.push([])
    for (let j = 0; j < matrix[i].length; j += 1) {
      visited[i][j] = false
    }
  }
  for (let i = 0; i < matrix.length; i += 1) {
    for (let j = 0; j < matrix[i].length; j += 1) {
      if (visited[i][j] === true || matrix[i][j] === 0) {
        continue
      }
      ans.push(bfs(matrix, visited, i, j))
    }
  }
  return ans
}

function bfs(matrix, visited, col, row) {
  const arr = [[col, row]]
  const temp = []
  visited[col][row] = true
  while (arr.length !== 0) {
    const cur = arr.shift()
    const cl = cur[0]
    const rw = cur[1]
    const child = [
      [cl - 1, rw],
      [cl + 1, rw],
      [cl, rw - 1],
      [cl, rw + 1],
    ]
    temp.push(cur)
    for (let i = 0; i < child.length; i += 1) {
      const node = child[i]
      if (
        node[0] >= 0 &&
        node[0] < matrix.length &&
        node[1] >= 0 &&
        node[1] < matrix[0].length
      ) {
        if (visited[node[0]][node[1]] === true) {
          continue
        }
        if (matrix[node[0]][node[1]] === 1) {
          arr.push(node)
          visited[node[0]][node[1]] = true
        }
      }
    }
  }
  return temp.length
}
exports.riverSizes = riverSizes

// 이어진 노드(1)의 크기를 구하는 문제
// 노드가 어디까지 이어진지 알 수 없으니까 bfs 탐색을 통해 인접한 노드중 가능한 노드를 모두 탐색해야함
