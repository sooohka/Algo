function isPalin(string = "") {
  if (!string) return false;
  for (let i = 0; i < string.length / 2; i += 1) {
    if (string[i] !== string[string.length - i - 1]) {
      return false;
    }
  }
  return true;
}

function longestPalindromicSubstring(string = "") {
  let ans = string[0];
  for (let i = 0; i < string.length; i += 1) {
    for (let j = i + 1; j <= string.length; j += 1) {
      const str = string.slice(i, j);
      if (isPalin(str) && str.length >= ans) {
        ans = str;
      }
    }
  }
  return ans;
}

/*
 * 가장 긴 팰린드롬을 구하는 문제
 * 앞뒤가 같으면 팰린드롬,
 * 1221, 121 모두 팰린드롬이 될 수 있음
 * 해결방법은
 * 1. substring을 모두 구한다.
 * 2. 구한 substring이 팰린드롬인지 비교한다.
 * 3. 팰린드롬인 substring 중 가장 빈 substring을 리턴
 */

exports.longestPalindromicSubstring = longestPalindromicSubstring;
