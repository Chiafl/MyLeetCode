from collections import OrderedDict, defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for x in s:
            d[x]+=1
        order = OrderedDict(sorted(d.items(),key=lambda item: item[1], reverse=True))
        val = ""
        for x in order:
            val = val+x*order[x]
        return val