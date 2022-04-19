function dfs(edges, visited, node) {
  const neighbors = edges[node];
  for (let i = 0; i < neighbors.length; i += 1) {
    if (visited[neighbors[i]]) {
      return true;
    }
    visited[neighbors[i]] = true;
    if (dfs(edges, visited, neighbors[i])) {
      return true;
    }
    visited[neighbors[i]] = false;
  }
  return false;
}

function cycleInGraph(edges) {
  const visited = edges.map(() => false);
  for (let i = 0; i < edges.length; i += 1) {
    if (dfs(edges, visited, i)) {
      console.log(visited);
      return true;
    }
  }
  return false;
}

/*
 * 그래프에 cycle이 있는지 확인하는 문제
 * dfs로 그래프를 도는데 노드를 방문할때마다 visited[노드]을 참값으로 바꿔줌
 * dfs순회중 visited[노드]가 참값이면 이미 방문했던 노드를 다시방문하는것임으로
 * 함수종료
 */
exports.cycleInGraph = cycleInGraph;
