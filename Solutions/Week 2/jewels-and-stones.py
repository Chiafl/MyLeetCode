import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set([j for j in J])
        stones = collections.Counter([s for s in S])
        return sum([stones[jewel] for jewel in jewels])