function spiralTraverse(array) {
  const arr = []
  let cR = 0
  let cC = 0
  let sR = 0
  let eR = array[0].length - 1
  let sC = 0
  let eC = array.length - 1
  const dir = ["r", "d", "l", "u"]
  let dirIdx = 0

  while (sR <= eR && sC <= eC) {
    if (dir[dirIdx % 4] === "r") {
      while (cR < eR) {
        arr.push(array[cC][cR])
        cR += 1
      }
      sC += 1
    } else if (dir[dirIdx % 4] === "d") {
      while (cC < eC) {
        arr.push(array[cC][cR])
        cC += 1
      }
      eR -= 1
    } else if (dir[dirIdx % 4] === "l") {
      while (cR > sR) {
        arr.push(array[cC][cR])
        cR -= 1
      }
      eC -= 1
    } else if (dir[dirIdx % 4] === "u") {
      while (cC > sC) {
        arr.push(array[cC][cR])
        cC -= 1
      }
      sR += 1
    }
    dirIdx += 1
  }
  arr.push(array[cC][cR])

  return arr
}
