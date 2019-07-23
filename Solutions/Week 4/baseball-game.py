class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        summy = 0
        for o in ops:
            if o=='C':
                summy -= stack.pop()
            elif o=='D':
                v = stack[-1]*2
                summy += v     
                stack.append(v)
            elif o=='+':
                v = stack[-1]+stack[-2]
                summy += v
                stack.append(v)
            else:
                summy += int(o)
                stack.append(int(o))
        return summy
            