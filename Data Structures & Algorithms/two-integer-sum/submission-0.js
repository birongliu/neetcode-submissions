class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
      const map = new Map();
      for(let i = 0; i < i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;
        const sumIndex = map.get(complement);
        const isTarget = map.has(complement);
        if(isTarget) return [i, sumIndex];
        map.set(num, i)
      }
      return [-1, -1]
    }
}
