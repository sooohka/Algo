function isPair(value, value2) {
  if (value === "(" && value2 === ")") {
    return true;
  }
  if (value === "[" && value2 === "]") {
    return true;
  }
  if (value === "{" && value2 === "}") {
    return true;
  }
  return false;
}

function balancedBrackets(string) {
  const stack = [];
  for (let i = 0; i < string.length; i += 1) {
    if (string[i] === "(" || string[i] === "[" || string[i] === "{") {
      stack.push(string[i]);
    } else if (string[i] === ")" || string[i] === "]" || string[i] === "}") {
      if (!isPair(stack.pop(), string[i])) {
        return false;
      }
    }
  }
  if (stack.length === 0) {
    return true;
  }
  return false;
}
