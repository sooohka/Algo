function kadanesAlgorithm(array) {
  let ans = array[0];
  const dp = new Array(array.length).fill(-Infinity);
  dp[0] = array[0];
  for (let i = 1; i < array.length; i += 1) {
    dp[i] = Math.max(dp[i - 1] + array[i], array[i]);
    ans = dp[i] > ans ? dp[i] : ans;
  }
  return ans;
}
/*
	인접한 숫자를 더해 나올수 있는 최대값을 구하는 문제
	각 인덱스별로 올 수 있는 최대값을 구하면됨 -> dp
*/

// Do not edit the line below.
exports.kadanesAlgorithm = kadanesAlgorithm;
