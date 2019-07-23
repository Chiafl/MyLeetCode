class LRUCache:

    def __init__(self, capacity: int):
        self.h = {}
        self.bot = None
        self.top = None
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        node = self.h[key]
        if node.top:
            node.top.bot = node.bot
        if node.bot:
            if node.top:
                node.bot.top = node.top            
        self.top = node
        if self.bot==node and node.top:
            self.bot = node.top
        self.top.top = None
        self.bot.bot = None
        print(self.h.keys(), self.bot.key, self.top.key)
        return self.top.val

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            node = self.h[key]
            node.val = value
            node.key = key
        else:
            node = ListNode(value)  
            node.key = key

        if not self.top:
            self.top = node
            self.bot = node
        elif self.top:
            self.top.top = node
            node.bot = self.top
            self.top = node
        if key not in self.h and len(self.h)==self.cap:
            k = self.bot.key
            print(key, self.h.keys(), self.bot.key, self.top.key)
            self.bot = self.bot.top
            if not self.bot:
                self.bot = node
            if k not in self.h:
                return
            print(k,self.h[k].val)
            del self.h[k]
            print(key, self.h.keys(), self.bot.key, self.top.key)


        self.h[key] = node
        self.top = node
        self.top.top = None
        self.bot.bot = None

class ListNode:
    
    def __init__(self, val):
        self.val = val
        self.key = None
        self.top = None
        self.bot = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)