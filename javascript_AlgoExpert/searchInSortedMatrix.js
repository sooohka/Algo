function searchInSortedMatrix(matrix, target) {
  if (matrix.length === 0) {
    return [-1, -1];
  }
  const height = matrix.length;
  const width = matrix[0].length;
  for (let i = height - 1; i >= 0; i -= 1) {
    if (matrix[i][0] > target) {
      continue;
    }
    for (let j = 0; j < width; j += 1) {
      if (matrix[i][j] === target) {
        return [i, j];
      }
      if (matrix[i][j] > target) {
        break;
      }
    }
  }
  return [-1, -1];
}
