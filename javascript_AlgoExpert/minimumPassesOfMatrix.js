function hasAdjacentPositive(matrix, c, r) {
  if (c - 1 >= 0 && matrix[c - 1][r] > 0) return true;
  if (c + 1 < matrix.length && matrix[c + 1][r] > 0) return true;
  if (r - 1 >= 0 && matrix[c][r - 1] > 0) return true;
  if (r + 1 < matrix[c].length && matrix[c][r + 1] > 0) return true;
  return false;
}

function getNegatives(matrix) {
  return matrix.reduce((pc, cc, ci) => {
    const c = cc.reduce((pr, cr, ri) => {
      if (cr < 0) return [...pr, [ci, ri]];
      return pr;
    }, []);
    return [...pc, ...c];
  }, []);
}

function minimumPassesOfMatrix(matrix) {
  let count = 0;
  let negatives = getNegatives(matrix);
  while (negatives.length !== 0) {
    const canChange = [];
    negatives = negatives.filter(([c, r]) => {
      if (hasAdjacentPositive(matrix, c, r)) {
        canChange.push([c, r]);
        return false;
      }
      return true;
    });
    if (canChange.length === 0) return -1;
    canChange.forEach(([c, r]) => {
      matrix[c][r] *= -1;
    });
    count += 1;
  }
  return count;
}
/*
 * matrix안에 음수를 모두 양수로 바꾸는 문제
 * 바뀌는 조건:음수 동서남북으로 양수가 있으면 다음턴에 양수로 바뀜
 * 1. 처음에 모든 음수를 구한다.
 * 2. 음수들에 대해 음수 주변에 양수가 있는지 확인 양수가 있으면 새 배열에 푸시
 * 3. 새배열에들어간 값들을 양수로 바꿈
 * 4. 위 과정 반복
 * 5. 시간복잡도 O(n^2)
 */
