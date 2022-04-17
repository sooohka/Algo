function minNumberOfCoinsForChange(n, denoms) {
  const dp = new Array(n + 1).fill(-1)
  dp[0] = 0
  for (let i = 1; i < n + 1; i += 1) {
    if (denoms.includes(i)) {
      dp[i] = 1
    } else {
      for (let j = i - 1; j >= 0; j -= 1) {
        if (dp[j] === -1 || dp[i - j] === -1) {
          continue
        }
        if (dp[i] === -1) {
          dp[i] = dp[j] + dp[i - j]
        } else {
          dp[i] = Math.min(dp[i], dp[j] + dp[i - j])
        }
      }
    }
  }
  return dp[n]
}

// Do not edit the line below.
exports.minNumberOfCoinsForChange = minNumberOfCoinsForChange
/*
배열의 인덱스를 코인의 크기라고 하자. 코인을 만들 수 있는 최소경우의 수를 배열으 인덱스에 채워준다.
채우는 방법은 현제 인덱스를 기준으로 전의 인덱스를 순회하며 dp[j]+d[i-j]의 최소값이 나오는 경우를
찾는다.
*/
