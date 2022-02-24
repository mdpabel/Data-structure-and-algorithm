`
1, 1, 2, 2, 2, 2, 3, 3

`;

function leftOccurrence(arr, key) {
  let left = 0;
  let right = arr.length - 1;

  let res = -1;
  while (left <= right) {
    const mid = left + ~~((right - left) / 2);
    if (arr[mid] == key) {
      right = mid - 1;
      res = mid;
    } else if (arr[mid] > key) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return res;
}

function rightOccurrence(arr, key) {
  let left = 0;
  let right = arr.length - 1;

  let res = -1;
  while (left <= right) {
    const mid = left + ~~((right - left) / 2);
    if (arr[mid] == key) {
      left = mid + 1;
      res = mid;
    } else if (arr[mid] > key) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return res;
}

const arr = [1, 1, 2, 2, 2, 2, 3, 3];
const left = leftOccurrence(arr, 2);
const right = rightOccurrence(arr, 2);

console.log(right - left + 1);
