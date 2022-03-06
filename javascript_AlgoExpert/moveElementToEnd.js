function moveElementToEnd(array, toMove) {
  function swap(array, a, b) {
    const temp = array[a];
    array[a] = array[b];
    array[b] = temp;
  }
  let front = 0;
  let back = array.length - 1;
  while (front < back) {
    while (front < back && array[back] === toMove) {
      back -= 1;
    }
    if (array[front] === toMove) swap(array, front, back);
    front += 1;
  }
  return array;
}

// Do not edit the line below.
exports.moveElementToEnd = moveElementToEnd;
