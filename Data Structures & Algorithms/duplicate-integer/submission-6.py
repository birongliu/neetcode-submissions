class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # the values of the nums and iterating over array the cost is O(n) and time complexity is O(n)
        duplicate = []
        for value in nums:
            if value in duplicate:
                return True
            else: 
                duplicate.append(value)
        return False