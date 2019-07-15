# Python solution recursive but not timed out in Leetcode

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        val = [nums[0]]
        iterator = iter(nums)
        next(iterator)
        for i, n in enumerate(iterator, start=1):
            if i<2:
                val.append(max(n, val[i-1]))
            else:
                val.append(max(n+val[i-2], val[i-1]))
        return val[-1]
        