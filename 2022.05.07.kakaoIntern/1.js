function solution(survey, choices) {
  let map = {
    A: 0,
    N: 0,
    C: 0,
    F: 0,
    J: 0,
    M: 0,
    R: 0,
    T: 0,
  };
  for (let i = 0; i < survey.length; i += 1) {
    if (choices[i] > 4) {
      map[survey[i][1]] += choices[i] - 4;
    } else if (choices[i] < 4) {
      map[survey[i][0]] += 4 - choices[i];
    }
  }
  let ans = "";
  ans += map.R >= map.T ? "R" : "T";
  ans += map.C >= map.F ? "C" : "F";
  ans += map.J >= map.M ? "J" : "M";
  ans += map.A >= map.N ? "A" : "N";
  return ans;
}
