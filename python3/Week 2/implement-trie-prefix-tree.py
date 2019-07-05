class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {}
        self.word = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self
        for w in word:
            if w not in node.node:
                node.node[w] = Trie()
            node = node.node[w]
        node.word = True
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for w in word:
            if w not in node.node:
                return False
            node = node.node[w]
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for p in prefix:
            if p not in node.node:
                return False
            node = node.node[p]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)