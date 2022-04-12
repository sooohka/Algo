function numberOfWaysToTraverseGraph(width, height) {
  const dp = [];
  for (let i = 0; i < height; i += 1) {
    dp.push([]);
    for (let j = 0; j < width; j += 1) {
      if (i === 0 || j === 0) {
        dp[i].push(1);
      } else {
        dp[i].push(0);
      }
    }
  }

  for (let i = 1; i < dp.length; i += 1) {
    for (let j = 1; j < dp[i].length; j += 1) {
      dp[i][j] = dp[i][j - 1] + dp[i - 1][j];
    }
  }
  return dp[height - 1][width - 1];
}

/*
	아래, 오른쪽으로 밖에 못감
	각 박스로 까지의 갈 수 있는 경로를 더한 뒤 도착박스의 위, 왼쪽 박스까지 갈수있는
	경로의 수를 더해주면 정답
*/
// Do not edit the line below.
exports.numberOfWaysToTraverseGraph = numberOfWaysToTraverseGraph;
