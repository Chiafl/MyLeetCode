class Solution:    
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        def vowel(c) -> bool:
            c = c.lower()
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                return True
            return False
        
        while i<j:
            if vowel(s[i]) and vowel(s[j]):
                s = s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
                i+=1
                j-=1
            else:
                if not vowel(s[i]):
                    i+=1
                if not vowel(s[j]):
                    j-=1
        return s