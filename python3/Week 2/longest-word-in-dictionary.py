class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = [{}, True]
        words = sorted(words)
        for w in words:
            temp = d
            for l in w:
                if l not in temp[0]:
                    temp[0][l] = [{}, False]
                    temp = temp[0][l]
                else:
                    temp = temp[0][l]
            temp[1] = True
        return self.depth(d, "", 0)[0]
            
    def depth(self, d, s, count):
        if not d[0]:
            return (s, count)
        elif d[1] == False:
            return (s[:-1], count-1)
        val = 0
        string = ""
        for x in d[0]:
            res = self.depth(d[0][x], s+x, count+1)
            if res[1]> val:
                (string, val) = (res[0], res[1])
        return (string, val)
            