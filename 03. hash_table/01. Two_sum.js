/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const map = {};
  for (let i = 0; i < nums.length; i++) {
    const currentMapVal = map[nums[i]];
    if (currentMapVal >= 0) {
      return [currentMapVal, i];
    } else {
      const required = target - nums[i];
      map[required] = i;
    }
  }
  return null;
};

const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSum(nums, target));
