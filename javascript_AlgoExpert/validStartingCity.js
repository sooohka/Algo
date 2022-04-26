function travel(distances, fuel, mpg, index) {
  let avaiableDistance = 0;
  for (let i = index; i < distances.length + index; i += 1) {
    const curLocIndex = i >= distances.length ? i - distances.length : i;
    avaiableDistance += fuel[curLocIndex] * mpg;
    avaiableDistance -= distances[curLocIndex];
    console.log(i, avaiableDistance);
    if (avaiableDistance < 0) {
      return false;
    }
    //
  }
  return true;
}

function validStartingCity(distances, fuel, mpg) {
  for (let i = 0; i < distances.length; i += 1) {
    if (travel(distances, fuel, mpg, i)) {
      return i;
    }
  }
  return -1;
}
/*
 */
