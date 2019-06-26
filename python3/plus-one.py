class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        r = 1
        for i in range(-1, -len(digits)-1, -1):
            if digits[i]+r >= 10:
                r = 1
                digits[i] = 0
            else:
                r = 0
                digits[i] = digits[i]+1
                break
        if r>0:
            digits.insert(0,r)
        return digits