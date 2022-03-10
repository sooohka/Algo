function arrayOfProducts(array) {
  const arr = [];
  const left = new Array().fill(1);
  const right = new Array().fill(1);

  let cur = 1;
  for (let i = 0; i < array.length; i += 1) {
    left[i] = cur;
    cur *= array[i];
  }
  cur = 1;
  for (let i = array.length - 1; i >= 0; i -= 1) {
    right[i] = cur;
    cur *= array[i];
  }
  for (let i = 0; i < array.length; i += 1) {
    arr.push(left[i] * right[i]);
  }
  return arr;
}

// 배열내 자기 자신외의 모든 값들을 곱해 새로운 배열을 만드는 문제
// for문을 돌려서 현재 인덱스를 기준으로 왼쪽에서는 현재 인덱스 오기 직전까지 모든 값을 곱함,
// 오른쪽에서는 현재 인덱스 오기 직전까지 모든 값을 곱함,
// 두 값을 곱함,
// 정답이 도출됨,
//
