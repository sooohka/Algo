function setMap(map) {
  map.set("1", ["1"]);
  map.set("2", ["a", "b", "c"]);
  map.set("3", ["d", "e", "f"]);
  map.set("4", ["g", "h", "i"]);
  map.set("5", ["j", "k", "l"]);
  map.set("6", ["m", "n", "o"]);
  map.set("7", ["p", "q", "r", "s"]);
  map.set("8", ["t", "u", "v"]);
  map.set("9", ["w", "x", "y", "z"]);
  map.set("0", ["0"]);
  return map;
}

function helper(map, pn, curIdx, ans, temp) {
  if (temp.length === pn.length) {
    ans.push(temp.join(""));
    return;
  }
  const currentValues = map.get(pn[curIdx]);
  for (let i = 0; i < currentValues.length; i += 1) {
    const newTemp = [...temp, currentValues[i]];
    helper(map, pn, curIdx + 1, ans, newTemp);
  }
}

function phoneNumberMnemonics(phoneNumber) {
  const ans = [];
  const map = new Map();
  setMap(map);
  helper(map, phoneNumber, 0, ans, []);
  return ans;
}
// Do not edit the line below.
exports.phoneNumberMnemonics = phoneNumberMnemonics;

/*
 * 조합문제(각 키마다 올수있는 값의 숫자가 다름)
 * 1. map자료구조를 사용해서 각 키마다 올수있는 값을 배열로 정의
 * 2. 재귀로 순회하면서 조합을 만듬(길이는 인자로 받은 스트링의 길이)
 * 3. 만든 조합의 길이가 스트링의 길이와 같으면 정답배열에 Push
 */
