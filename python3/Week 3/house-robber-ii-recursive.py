class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        val1 = self.helper(nums[:-1])
        val2 = self.helper(nums[1:])
        return max(val1, val2)
    
    def helper(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return max(nums[0]+self.helper(nums[2:]), self.helper(nums[1:]))