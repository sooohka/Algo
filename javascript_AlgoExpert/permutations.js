// sol1
function dfs(array, visited, ans, temp) {
  if (temp.length === array.length) {
    ans.push([...temp]);
    return;
  }

  for (let i = 0; i < array.length; i += 1) {
    if (visited[i]) {
      continue;
    }
    visited[i] = true;
    temp.push(array[i]);
    dfs(array, visited, ans, temp);
    temp.pop();
    visited[i] = false;
  }
}
function getPermutations(array) {
  if (array.length === 0) return [];
  const visited = new Array(array.length).fill(false);
  console.log(visited);
  const ans = [];
  dfs(array, visited, ans, []);
  return ans;
}

// sol2
function helper(array, ans, temp) {
  if (array.length === 0) {
    ans.push(temp);
  }
  array.forEach((v, i) => {
    const newA = [...array.slice(0, i), ...array.slice(i + 1)];
    const cur = [...temp, array[i]];
    helper(newA, ans, cur);
  });
}

function getPermutations(array) {
  const ans = [];
  if (array.length === 0) {
    return [];
  }
  helper(array, ans, []);
  return ans;
}

/*
 * 조합문제,,
 * sol1 방문배열 사용해서 방문하지 않은 노드에 대해서만 추가해줌
 * sol2 재귀함수를 도는데 방문한 값을 배열에서 제외하고 기존 배열자리에 인자로
 * 넘겨줘서 배열의 길이가 0까지 이를 반복함
 */
