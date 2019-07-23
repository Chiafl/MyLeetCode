class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        visited = {}
        return self.helper(nums, 0, sum(nums), 0, visited)
        
    def helper(self, n1, v1, v2, idx, visited):
        if v1 in visited:
            return False
        if v1==v2:
            return True
        if len(n1)<=idx:
            return False
        
        visit = (self.helper(n1, v1+n1[idx], v2-n1[idx], idx+1, visited)
            or self.helper(n1, v1, v2, idx+1, visited))
        visited[v1] = visit
        if visit:
            return True
        
            