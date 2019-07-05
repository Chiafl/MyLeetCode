import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("[ ]{2,}"," ",re.sub("[^\w ]"," ", paragraph.lower()))
        ls = paragraph.split(' ')
        C = collections.Counter([l for l in ls if l not in banned])
        return C.most_common(1)[0][0]
