function helper(array, ans, temp) {
  ans.push(temp);
  for (let i = 0; i < array.length; i += 1) {
    const a = [...array.slice(i + 1, array.length)];
    helper(a, ans, [...temp, array[i]]);
  }
}

function powerset(array) {
  const ans = [];
  helper(array, ans, []);
  return ans;
}

/*
 * 모든 조합의 수를 구하는 문제
 * 순열을 돌때처럼 재귀함수를 돌리는데 순열과 달리 [1,2,3],[3,2,1]을 동일한
 * 조합으로 보기 때문에 현재 인덱스 기준 뒤에값들만 push해주어야함
 */
exports.powerset = powerset;
