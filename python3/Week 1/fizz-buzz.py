class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        A = []
        for a in range(1, n+1):
            s = ''
            if a%3==0:
                s = s+'Fizz'
            if a%5==0:
                s = s+'Buzz'
            if s == '':
                s = str(a)
            A.append(s)
        return A
            