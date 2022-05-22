function minimumCharactersForWords(words) {
  const arr = [];
  const obj = {};
  for (const item of words) {
    helper(obj, item);
  }
  Object.keys(obj).forEach((key) => {
    for (let i = 0; i < obj[key]; i += 1) {
      arr.push(key);
    }
  });

  return arr;
}

function helper(obj, word) {
  const j = {};
  for (let i = 0; i < word.length; i += 1) {
    if (j[word[i]]) {
      j[word[i]] += 1;
    } else {
      j[word[i]] = 1;
    }
    if (!obj[word[i]]) {
      obj[word[i]] = j[word[i]];
    } else {
      obj[word[i]] = Math.max(j[word[i]], obj[word[i]]);
    }
  }
}
