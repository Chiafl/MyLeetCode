class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {x:y for x,y in enumerate([".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        S = set()
        for word in words:
            S.add(str("".join([morse[(ord(letter)-ord('a'))] for letter in word])))
        return len(S)