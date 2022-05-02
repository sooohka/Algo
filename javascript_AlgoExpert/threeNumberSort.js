function swap(array, i, j) {
  const temp = array[i];
  array[i] = array[j];
  array[j] = temp;
}

function firstSort(array, order) {
  let i = 0;
  let j = array.length - 1;
  while (i < array.length && j >= 0 && i < j) {
    while (i < array.length - 1 && array[i] === order[0]) {
      i += 1;
    }
    while (j > 0 && (array[j] === order[1] || array[j] === order[2])) {
      j -= 1;
    }
    if (array[i] !== order[0] && array[j] === order[0] && i < j) {
      swap(array, i, j);
    }
  }
}

function secondSort(array, order) {
  let i = 0;
  let j = array.length - 1;
  while (i < array.length && j >= 0 && i < j) {
    // order[0]인경우 그냥 밀자
    while (i < array.length - 1 && array[i] === order[0]) {
      i += 1;
    }
    while (i < array.length - 1 && array[i] === order[1]) {
      i += 1;
    }
    while (j > 0 && array[j] === order[2]) {
      j -= 1;
    }
    if (array[i] === order[2] && array[j] === order[1] && i < j) {
      swap(array, i, j);
    }
  }
}

function threeNumberSort(array, order) {
  firstSort(array, order);
  secondSort(array, order);
  return array;
}
