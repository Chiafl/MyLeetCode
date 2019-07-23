class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ls = [0 for i in range(len(nums))]
        for i in nums:
            if i<1 or i>len(nums):
                break
            ls[i-1]+=1
        twice = 0
        wrong = 0
        for i,x in enumerate(ls):
            if x==2:
                twice = i+1
            elif x==0 and wrong==0:
                wrong = i+1
        return [twice, wrong]
        
        