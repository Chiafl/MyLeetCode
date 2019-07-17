class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        windowSize = len(p)
        sortP = sorted(p)
        sortS = sorted(s[:windowSize])
        ls = []
        for i in range(len(s)-windowSize+1):
            if sortP == sortS:
                ls.append(i)
            if i<len(s)-windowSize and s[i]!=s[i+windowSize]:
                sortS = self.binaryRemove(sortS, s[i])
                sortS = self.binaryInsert(sortS, s[i+windowSize])
        return ls
    
    def binaryRemove(self, s, c):
        low = 0
        high = len(s)-1
        while (low<=high):
            mid = low+(high-low)//2
            if (s[mid]==c):
                return s[:mid]+s[mid+1:]
            elif (s[mid]<c):
                low = mid+1
            else:
                high = mid-1
        return -1
    
    def binaryInsert(self, s, c):
        low = 0
        high = len(s)-1
        res = -1
        while (low<=high):
            mid = low+(high-low)//2
            if (s[mid]==c):
                res = mid
                low = mid+1
            elif (s[mid]<c):
                low = mid+1
            else:
                high = mid-1
        if res!=-1:
            return s[:res]+[c]+s[res:]
        elif low<len(s):
            return s[:low]+[c]+s[low:]
        else:
            return s+[c]
