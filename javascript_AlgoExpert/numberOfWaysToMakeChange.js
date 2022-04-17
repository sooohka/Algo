function numberOfWaysToMakeChange(n, denoms) {
  const dp = new Array(n + 1).fill(0)
  dp[0] = 1
  for (const denom of denoms) {
    for (let i = denom; i < n + 1; i += 1) {
      dp[i] += dp[i - denom]
    }
  }
  return dp[n]
}

// Do not edit the line below.
exports.numberOfWaysToMakeChange = numberOfWaysToMakeChange
/*
 dp배열의 인덱스 i를 denoms로 i원을 만들수 있는 경우의 수라고 하자.
그러면 예를 들어 10을 만드는데의 경우의 수는 dp[1]가 만들어지는 경우의 수
+ dp[9]가 만들어지는 경우의수, dp[2] dp[8], ... 이렇게 갈것이다.
denoms를 활용해서 각 숫자(i)가 만들어지는 경우의 수를 구하면 정답이다.
	*/
