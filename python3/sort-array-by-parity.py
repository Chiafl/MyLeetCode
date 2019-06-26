class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return list(filter(lambda x: x%2==0, A))+list(filter(lambda x: x%2==1, A))