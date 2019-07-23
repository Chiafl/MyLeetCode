class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        v = 0
        for n in nums:
            v ^= n
        return v