# Mergesort in Python results in a runtime error
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums) #self.mergeSort(nums)
        s = 0
        for i in range(0,len(nums),2):
            s += min(nums[i], nums[i+1])
        return s
        
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        return self.merge(self.mergeSort(nums[0:len(nums)//2]),
                          self.mergeSort(nums[len(nums)//2:len(nums)]))
    
    def merge(self, n1:List[int], n2:List[int]) -> List[int]:
        if not n1:
            return n2
        if not n2:
            return n1
        if n1[0]<n2[0]:
            return [n1[0]]+self.merge(n1[1:], n2)
        else:
            return [n2[0]]+self.merge(n1, n2[1:])
            