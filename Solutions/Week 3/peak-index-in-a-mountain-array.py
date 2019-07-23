class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 0
        j = len(A)-1
        while i<=j:
            mid = i+(j-i)//2
            if A[mid-1]<A[mid] and A[mid]>A[mid+1]:
                return mid
            elif A[mid-1]<A[mid] and A[mid]<A[mid+1]:
                i = mid+1
            else:
                j = mid-1
        return -1