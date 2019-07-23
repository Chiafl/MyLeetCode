import collections

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if not self.q1 and not self.q2:
            self.q1.append(x)
        elif not self.q1:
            self.q2.append(x)
        else:
            self.q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.q1:
            for i in range(len(self.q1)-1):
                self.q2.append(self.q1.popleft())
            return self.q1.popleft()
        else:
            for i in range(len(self.q2)-1):
                self.q1.append(self.q2.popleft())
            return self.q2.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q1:
            return self.q2[-1]
        else:
            return self.q1[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1)==0 and len(self.q2)==0
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()