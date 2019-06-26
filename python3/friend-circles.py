class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def merge(L1: List[int], L2: List[int]) -> List[int]:
            L = []
            for i in range(0, len(L1)):
                L.append(L1[i]|L2[i])
            return L
        def common(L1: List[int], L2: List[int]) -> bool:
            for i in range(0, len(L1)):
                if L1[i]==1 and L2[i]==1:
                    return True
            return False
        
        n = len(M)
        for i in range(0, n):
            for j in range(0, n):
                if i==j:
                    continue
                if common(M[i], M[j]):
                    M[i] = merge(M[i],M[j])
                    M[j] = [0]*n
        print(M)
        while [0]*n in M:
            M.remove([0]*n)    
        return len(M)
                    
            
                
