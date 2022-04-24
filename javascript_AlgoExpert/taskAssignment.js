function toObjs(tasks) {
  return tasks.map((task, i) => ({value: task, idx: i}));
}
function taskAssignment(k, tasks) {
  const combi = [];
  // always 2k
  const sorted = toObjs(tasks).sort((a, b) => (a.value > b.value ? 1 : -1));
  for (let i = 0; i < sorted.length / 2; i += 1) {
    combi.push([sorted[i].idx, sorted[sorted.length - i - 1].idx]);
  }
  return combi;
}

const k = 3; // num of worker
const tasks = [1, 3, 5, 3, 1, 4]; // due time of worker, always 2k

/*
 * k수의 일꾼들이 과제들 끝낼 수 있는 최적의 조합 찾기,
 * 일꾼은 한번에 하나의 과제 할 수 있고, 총 두 과제를 끝내면 됨
 * 1. 배열내 값을 obj로 변경,obj는 idx와 value 를 가짐
 * 2. obj들을 value를 사용해서 정렬
 * 3. 정렬한 배열을 반으로 쪼개 맨 앞값과 맨 뒷값으로 짝을지어줌
 */
