class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const duplicate = new Set();
        for(const num of nums) {
            if(duplicate.has(num)) {
                return true;
            }
            duplicate.add(num)
        }
        return false
    }
}
