# Used sliding window technique, but solving using in-built sort function was too expensive to pass all
# test cases due to time out

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        windowSize = len(p)
        sortP = sorted(p)
        sortS = sorted(s[:windowSize])
        ls = []
        for i in range(len(s)-windowSize):
            if sortP == sortS:
                ls.append(i)
            if i+1<len(s):
                sortS = sorted(s[i+1:i+windowSize+1])
        return ls