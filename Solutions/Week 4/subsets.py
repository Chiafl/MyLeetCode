class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ls = [[]]
        self.helper(nums, ls)
        return ls
        
    def helper(self, nums, ls):
        if nums not in ls:
            ls.append(nums)
        else:
            return
        for x in range(len(nums)):
            self.helper(nums[:x]+nums[x+1:], ls)
        return