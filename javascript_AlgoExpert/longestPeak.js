function longestPeak(array) {
  let highest = 0;
  for (let i = 1; i < array.length - 1; i += 1) {
    let count = 1;
    let j = i;
    const isPeak = array[i - 1] < array[i] && array[i] > array[i + 1];
    if (!isPeak) continue;
    while (j > 0 && array[j] > array[j - 1]) {
      count += 1;
      j -= 1;
    }
    j = i;
    while (j < array.length - 1 && array[j] > array[j + 1]) {
      count += 1;
      j += 1;
    }
    if (highest < count) highest = count;
  }
  console.log(highest);
  return highest;
}
// 이 문제는 우선 가장 긴 픽을 찾는 문제입니다.
// 저는 이문제를 해결하기 위해서는 우선 peak의 꼭대기를 먼저 찾을것 같습니다.
// 그러기 위해서 for문을 돌면서 모든 요소를 순회하는데 1번째 인덱스 부터 array.length - 1번째
// 까지 순회합니다. 왜냐하면 peak은 최소 3개의 요소를 포함하기 때문입니다.
// for문을 돌면서 모든 요소가 peak이 될 가능성이 있는지를 판단합니다.
// 그러기 위해서 바로 직전요소가 현재 요소보다 작고 바로 다음요소가 현재 요소보다 작은지를 판단합니다.
// peak이 될 가능성이 없으면 continue로 넘어가고
// peak이 될 가능성이 있으면 두개의 while문을 실행하는데 이 while문으로 현재요소까지 증가하는데
// 필요한 값들을 세주고, 현재 요소에서 어디까지 감소하는지를 세줍니다.
// 세준 이 두개의 값을 더하면 이 값이 peak의 길이가 됩니다.
//
