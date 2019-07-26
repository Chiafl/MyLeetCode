import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d.update({n:d.get(n, 0)+1})
        
        ls = []
        for item in d.items():
            heapq.heappush(ls, (item[1], item[0]))
            if len(ls)>k:
                heapq.heappop(ls)
    
        ls = list(map(lambda x: x[1], ls))
        ls.reverse()
        return ls