class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False
                elif stack.pop()+char not in ('()','[]','{}'):
                    return False
        if stack:
            return False
        return True