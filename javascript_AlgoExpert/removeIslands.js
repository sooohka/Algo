function removeIslands(matrix) {
  const visited = matrix.map((row) => row.map(() => false))
  const newMatrix = matrix.map((row) => row.map(() => 0))
  for (let i = 0; i < matrix.length; i += 1) {
    bfs(matrix, newMatrix, visited, i, 0)
    bfs(matrix, newMatrix, visited, i, matrix[0].length - 1)
  }
  for (let i = 0; i < matrix[0].length; i += 1) {
    bfs(matrix, newMatrix, visited, 0, i)
    bfs(matrix, newMatrix, visited, matrix.length - 1, i)
  }
  return newMatrix
}

function bfs(matrix, newMatrix, visited, col, row) {
  if (matrix[col][row] !== 1) {
    return
  }
  const arr = [[col, row]]
  newMatrix[col][row] = 1
  visited[col][row] = true
  while (arr.length !== 0) {
    const cur = arr.shift()
    const c = cur[0]
    const r = cur[1]
    const possibles = [
      [c - 1, r],
      [c + 1, r],
      [c, r + 1],
      [c, r - 1],
    ]
    for (const p of possibles) {
      const [pc, pr] = p
      if (pc >= matrix.length || pc < 0 || pr >= matrix[0].length || pr < 0) {
        continue
      }
      if (visited[pc][pr] === true) {
        continue
      }
      if (matrix[pc][pr] === 1) {
        arr.push([pc, pr])
        newMatrix[pc][pr] = 1
        visited[pc][pr] = true
      }
    }
  }
}
/*
 * border에 대해서 bfs탐색을 해주고 땅이 있으면
 * 자리에 1 할당, 나머지는 모두 0할당
 * */

// Do not edit the line below.
exports.removeIslands = removeIslands
