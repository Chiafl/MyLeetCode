import collections

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        for i in range(len(cpdomains)):
            cpdomains[i] = cpdomains[i].split(" ")
        C = collections.Counter()
        for i,x in enumerate(cpdomains):
            while x[1]:
                index = x[1].find('.')
                C.update({x[1]:int(x[0])})
                if index!=-1:
                    cpdomains[i][1] = x[1][index+1:]
                else:
                    cpdomains[i][1] = ""
        ls = []
        for x in C:
            ls.append(str(C[x])+" "+x)
        return ls
