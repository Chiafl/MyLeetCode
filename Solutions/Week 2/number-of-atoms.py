# I struggled a lot on this question. Originally attempted to solve this recursively
# but had a difficult time keeping track of everything so opted for iterative stack solution
# Inefficient memory usage

import collections
import re

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        S = []
        s = formula
        while s.find('(')>=0 and s.find(')')>=0:
            s = re.sub("\([\w]*\)[\d]*","",s)
        D = self.extract(s)
        i = 0
        k = 0
        n = len(formula)
        C = collections.Counter()
        for j in range(n+1):
            if j==n:
                break
            if formula[j]=='(':
                stack.append(j+1)
                S.append(collections.Counter())
            elif formula[j]==')':
                if stack and S:
                    prev = i
                    i = stack.pop()
                    s = formula[i:j]
                    v = ""
                    p = S.pop()
                    while j+1<n and (formula[j+1]>='0' and formula[j+1]<='9'):
                        v = v+formula[j+1]
                        j+=1
                    if not v:
                        if i<prev:
                            while s.find('(')>=0 and s.find(')')>=0:
                                s = re.sub("\([\w]*\)[\d]*","",s)
                            if not S:
                                C = C+ p + self.extract(s)
                            else:
                                S[-1] = p + self.extract(s)
                        else:
                            if not S:
                                C = C + p + self.extract(s)
                            else:
                                S[-1] = S[-1]+ p + self.extract(s)
                    else:
                        if i<prev:
                            while s.find('(')>=0 and s.find(')')>=0:
                                s = re.sub("\([\w]*\)[\d]*","",s)
                            if not S:
                                C = C + self.mult(p+self.extract(s), int(v))
                            else:
                                S[-1] = S[-1] + self.mult(p+self.extract(s), int(v))
                        else:
                            if not S: 
                                C = C+ p + self.mult(self.extract(s), int(v)) 
                            else:
                                S[-1] = S[-1]+ p + self.mult(self.extract(s), int(v)) 
        C = C + D
        C = sorted(C.items(), key=lambda x: x[0], reverse=False)
        return "".join([x+str(y) if y!=1 else x for x,y in C])

    # Get counts of values
    def extract(self, S:str):
        temp = collections.Counter()
        S = re.sub("([A-Z][a-z]?)([\d]*)", "\\1,\\2 ", S)
        ls = [s.split(',') for s in S.split()]
        for l in ls:
            if not l[1]:
                temp.update({l[0]:1})
            else:
                temp.update({l[0]:int(l[1])})
        return temp
    
    # Multiply everything within parenthesis
    def mult(self, C, x):
        temp = collections.Counter()
        for a in C:
            temp[a] = C[a]*x
        return temp
        
        