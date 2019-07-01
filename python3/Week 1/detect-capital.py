class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        
        #corresponds to rule 1,2,3, respectively
        rules = [True, True, True]
        
        if word[0]>='A' and word[0]<='Z':
            rules[1] = False
        else:
            rules[0] = False
            rules[2] = False
            
        for i in range(1, len(word)):
            if word[i]>='A' and word[i]<='Z':
                rules[1]=False
                rules[2]=False
            else:
                rules[0]=False
            if not rules[0] and not rules[1] and not rules[2]:
                return False
        return True