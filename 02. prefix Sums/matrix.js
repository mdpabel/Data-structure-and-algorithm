/**
  1 2 3 4 5 0
  6 7 8 9 0 4
  1 2 3 4 5 3
  6 7 8 9 0 2
  1 2 3 4 5 1

 */

function regionSum(matrix) {
  const ROWS = matrix.length,
    COLS = matrix[0].length;

  const prefixSum = [];

  for (let i = 0; i < ROWS + 1; i++) {
    rowPrefixSum = [];
    for (let j = 0; j < COLS + 1; j++) {
      rowPrefixSum.push(0);
    }
    prefixSum.push(rowPrefixSum);
  }

  for (let i = 0; i < ROWS; i++) {
    let prefix = 0;
    for (let j = 0; j < COLS; j++) {
      prefix += matrix[i][j];
      let above = prefixSum[i][j + 1];
      prefixSum[i + 1][j + 1] = prefix + above;
    }
  }

  console.log(prefixSum);
}

const matrix = [
  [1, 2, 3, 4, 5, 0],
  [6, 7, 8, 9, 0, 4],
  [1, 2, 3, 4, 5, 3],
  [6, 7, 8, 9, 0, 2],
  [1, 2, 3, 4, 5, 1],
];

regionSum(matrix);
