class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        i = 0
        pre = ""
        while i<len(strs[0]):
            for k in range(1, len(strs)):
                if i>=len(strs[k]) or strs[k][i]!=strs[k-1][i]:
                    return pre
            pre = pre+strs[0][i]
            i+=1
        return pre