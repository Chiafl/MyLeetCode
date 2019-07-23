class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ls = []
        self.helper(nums, ls, [], len(nums))
        return ls
    
    def helper(self, nums, ls, temp, k):
        if k==len(temp):
            ls.append(temp)
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], ls, temp+[nums[i]], k)