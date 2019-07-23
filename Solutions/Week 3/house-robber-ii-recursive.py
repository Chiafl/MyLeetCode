class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        ls1 = []
        ls2 = []
        self.helper(nums[:-1], ls1)
        self.helper(nums[1:], ls2)
        return max(ls1[-1], ls2[-1])
    
    def helper(self, nums: List[int], ls: List[int]) -> int:
        if not nums:
            return
        if not ls:
            ls.append(nums[0])
        elif len(ls)==1:
            ls.append(max(nums[0],ls[-1]))
        else:
            ls.append(max(ls[-1],nums[0]+ls[-2]))
        return self.helper(nums[1:],ls)