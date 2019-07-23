class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ls = []
        self.helper(candidates, target, [], 0, ls)
        return ls
        
    def helper(self, candidates, target, temp, v, ls):
        if v == target:
            ins = sorted(temp)
            if ins not in ls:
                ls.append(ins)
            return
        for n in candidates:
            if n+v<=target:
                self.helper(candidates, target, temp+[n], v+n,ls)
        
        