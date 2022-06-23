const arr = [1, 6, 4, 2, 5, 3];

const prefix_sum = [];

prefix_sum.push(arr[0]);

for (let i = 1; i < arr.length; i++) {
  prefix_sum.push(arr[i] + prefix_sum[i - 1]);
}

console.log(prefix_sum);
