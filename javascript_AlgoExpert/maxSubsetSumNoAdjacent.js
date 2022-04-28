function maxSubsetSumNoAdjacent(array) {
  const dp = [...array];

  dp.fill(0, 0, array.length);
  if (array.length === 0) {
    return 0;
  }
  if (array.length === 1) {
    return array[0];
  }
  dp[0] = array[0];
  dp[1] = Math.max(array[0], array[1]);
  for (let i = 2; i < array.length; i += 1) {
    if (dp[i - 2] + array[i] > dp[i - 1]) {
      dp[i] = dp[i - 2] + array[i];
    } else {
      dp[i] = dp[i - 1];
    }
  }
  return Math.max(...dp);
}
/*
 배열의 각 인덱스 별로 올 수 있는 최대값을 구해야하기 때문(현재 인덱스로 오기전까지의 값이 중요함)에
dp를 사용해야된다고 생각했다.
인덱스가 인접하면 안되기 때문에 현재 인덱스에 올 수 있는 값은
1. dp[i - 2] + array[i]
2. dp[i - 1]
일 수 밖에 없다.
위 점화식을 코드로 구현했다.
*/
