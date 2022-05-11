function insertToStack(stack, value) {
  if (stack.length === 0) {
    stack.push(value);
    return;
  }

  const top = stack.pop();
  if (top <= value) {
    stack.push(top);
    stack.push(value);
    return;
  }
  if (top > value) {
    insertToStack(stack, value);
    stack.push(top);
  }
}

function sortStack(stack) {
  if (stack.length === 0) return stack;

  const top = stack.pop();

  sortStack(stack);

  insertToStack(stack, top);

  return stack;
}
