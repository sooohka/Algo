function smallestDifference(arrayOne, arrayTwo) {
  let ans = [arrayOne[0], arrayTwo[0]];
  arrayOne.forEach((v) => {
    arrayTwo.forEach((v2) => {
      const AD = Math.abs(v - v2);
      const prevAD = Math.abs(ans[0] - ans[1]);
      if (prevAD > AD) ans = [v, v2];
    });
  });
  return ans;
}

//better solution
function smallestDifference(arrayOne, arrayTwo) {
  arrayOne.sort((a, b) => a - b);
  arrayTwo.sort((a, b) => a - b);
  let oneIdx = 0;
  let twoIdx = 0;
  let ans = [arrayOne[0], arrayTwo[0]];

  while (oneIdx < arrayOne.length && twoIdx < arrayTwo.length) {
    if (arrayOne[oneIdx] < arrayTwo[twoIdx]) {
      oneIdx += 1;
    } else {
      twoIdx += 1;
    }
    const prev = Math.abs(ans[0] - ans[1]);
    const cur = Math.abs(arrayOne[oneIdx] - arrayTwo[twoIdx]);
    if (prev > cur) ans = [arrayOne[oneIdx], arrayTwo[twoIdx]];
  }

  return ans;
}

// Do not edit the line below.
exports.smallestDifference = smallestDifference;
