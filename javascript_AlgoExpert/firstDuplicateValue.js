function firstDuplicateValue(array) {
  const dict = {}
  for (const val of array) {
    if (dict[val] === undefined) dict[val] = true
    else return val
  }
  return -1
}
// 처음으로 겹치는 숫자를 찾는 문제.
// 딕셔너리를 사용하면 편할것 같아서 딕셔너리를 사용함.
// for 문을 통해  array의 모든값을 순회하면서 모든 값을 검사
// 값이 딕셔너리에 없으면 딕셔너리에 key로 값을 추가
// 값이 딕셔너리에 key로 존재하면 전에 값이 나왔단 소리임으로 그 값을 리턴함
