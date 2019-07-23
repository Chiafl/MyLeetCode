class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(0, (len(s)+1)//2):
            temp = s[i]
            s[i] = s[-i-1]
            s[-i-1] = temp
        """
        Do not return anything, modify s in-place instead.
        """