class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k = k%n
        curr = 0
        start = 0
        cnt = 0
        i = 0
        while (cnt<n):
            nxt = (i+k)%n
            start, curr = i, i
            prev = nums[curr]
            while nxt!=start:      
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                curr = nxt
                nxt = (nxt+k)%n
                cnt+=1
            nums[nxt] = prev
            cnt+=1
            i+=1
        return nums
        
