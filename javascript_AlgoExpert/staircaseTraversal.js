// 재귀함수로 풀이한 풀이
// O(maxSteps^height)
function helper(steps, height, ans, temp) {
  // TODO
  const sum = temp.reduce((p, c) => p + c, 0);
  if (sum > height) {
    return;
  }
  if (sum === height) {
    ans.push(temp);
    return;
  }
  for (let i = 0; i < steps.length; i += 1) {
    const newTemp = [...temp, steps[i]];
    helper(steps, height, ans, newTemp);
  }
}

function staircaseTraversal(height, maxSteps) {
  const steps = [];
  if (maxSteps === 0) {
    return 0;
  }
  for (let i = 1; i <= maxSteps; i += 1) {
    steps.push(i);
  }
  const ans = [];
  helper(steps, height, ans, []);
  return ans.length;
}

// 재귀 + dp로 풀이한 문제
// O(maxSteps * height);
function helper(height, maxSteps, dp) {
  if (dp[height] !== 0) return dp[height];
  for (let i = height - 1; i >= height - maxSteps; i -= 1) {
    if (i < 0) continue;
    dp[height] += helper(i, maxSteps, dp);
  }
  return dp[height];
}

function staircaseTraversal(height, maxSteps) {
  if (height === 0 || height === 1) return 1;
  const dp = new Array(height + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;
  helper(height, maxSteps, dp);
  return dp[height];
}

// dp 사용한 풀이
// O(height*maxSteps)
function staircaseTraversal(height, maxSteps) {
  if (height === 0 || height === 1) {
    return 1;
  }
  const dp = new Array(height + 1).fill(0);
  dp[0] = 1;
  dp[1] = 1;
  for (let i = 2; i <= height; i += 1) {
    for (let j = i; j >= i - maxSteps; j -= 1) {
      if (j < 0) {
        break;
      }
      dp[i] += dp[j];
    }
  }
  return dp[height];
}

// Do not edit the line below.
// exports.staircaseTraversal = staircaseTraversal;
/*
 * 한번에 오를수 있는 계단의 수와 높이가 주어졌을때 계단을 오를수있는
 * 모든 경우의 수를 구하는 순열문제
 */
