function sunsetViews(buildings, direction) {
  if (buildings.length === 0) {
    return [];
  }
  const endIdx = buildings.length - 1;
  const answer = [];
  switch (direction) {
    case "EAST": {
      let tallestIdx = endIdx;
      answer.push(endIdx);
      for (let i = endIdx - 1; i >= 0; i -= 1) {
        if (buildings[tallestIdx] < buildings[i]) {
          answer.push(i);
          tallestIdx = i;
        }
      }
      answer.reverse();
      return answer;
    }
    case "WEST": {
      let tallestIdx = 0;
      answer.push(0);
      for (let i = 1; i <= endIdx; i += 1) {
        if (buildings[tallestIdx] < buildings[i]) {
          answer.push(i);
          tallestIdx = i;
        }
      }
      return answer;
    }
    default: {
      return [];
    }
  }
}

const buildings = [3, 5, 4, 4, 3, 1, 3, 2];
const direction = "EAST";

console.log(sunsetViews(buildings, direction));
