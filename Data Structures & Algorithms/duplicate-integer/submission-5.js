class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // hash map to keep track of nums if it had value; if not than not a duplicate; if it is then it dup
        let hashmap = {};
        for(let i = 0; i < nums.length; i++) {
            if(hashmap[nums[i]] === nums[i]) return true;
            hashmap[nums[i]] = nums[i]
        }
        return false;
    }
}
