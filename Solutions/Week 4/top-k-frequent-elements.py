import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        C = collections.Counter(nums)
        return list(map(lambda x: x[0], C.most_common(k)))