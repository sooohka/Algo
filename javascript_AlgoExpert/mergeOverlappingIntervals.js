function mergeOverlappingIntervals(array) {
  const ans = [];
  array.sort((a, b) => a[0] - b[0]);
  for (let i = 0; i < array.length - 1; i += 1) {
    const cur = array[i];
    const next = array[i + 1];
    //not overlap
    if (cur[1] < next[0]) {
      ans.push(cur);
    }
    //overlap
    else {
      array[i + 1] = [cur[0], Math.max(cur[1], next[1])];
    }
  }
  ans.push(array[array.length - 1]);
  return ans;
}
// 2차원 배열m의 요소중 overlap되는 요소(m[k])를 머지하는 문제
// 이때, overlap은 m[k][1]이 m[k+1][0]보다 큰 경우를 말함
// for문을 돌건데 이때 overlap되는 경우와 overlap되지 않는 경우를 나눠서 분기함
// 1. overlap되는 경우
//     overlap되는 경우에는 다음 요소 m[k+1]에 overlap된 결과물을 할당함 이때 주의해야될 점은
//     m[k+1][1]이 m[k][1]보다 항상 크지 않음으로 이 두값을 비교한 뒤 큰값을 할당해야함
//     m[k+1] = [m[k][0],Math.max(m[k+1][1],m[k][1])]
// 2. overlap 되지 않는 경우
//     overlap되지 않는 경우에는 단순히 현재 요소 k를 정답배열에 푸시함
