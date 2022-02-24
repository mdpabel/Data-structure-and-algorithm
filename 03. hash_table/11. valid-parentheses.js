/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (str) {
  const stack = [];
  const map = {
    ")": "(",
    "}": "{",
    "]": "[",
  };

  for (const item of str) {
    if (item == "(" || item == "{" || item == "[") {
      stack.push(item);
    } else if (stack.pop() != map[item]) {
      return false;
    }
  }
  return !stack.length;
};
