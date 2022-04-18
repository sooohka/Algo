function groupAnagrams(words = []) {
  const parsed = words.map((word, idx) => {
    const sorted = Array.from(word).sort().join("");
    return {word, sorted};
  });

  const dict = new Map();
  parsed.forEach((word) => {
    if (dict.get(word.sorted)) {
      dict.get(word.sorted).push(word);
    } else {
      dict.set(word.sorted, [word]);
    }
  });
  const ans = Array.from(dict.keys()).map((key) =>
    dict.get(key).map((v) => v.word)
  );
  return ans;
}
/*
 * 아나그램을 찾아서 같은것 끼리 묶고 리턴하는 문제
 */

// Do not edit the line below.
exports.groupAnagrams = groupAnagrams;
