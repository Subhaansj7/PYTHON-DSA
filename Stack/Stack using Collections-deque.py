from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
        
    def is_empty(self):
        return len(self.container) == 0
        
    def size(self):
        return len(self.container)
        
#driver code 
s=Stack()
s.push(5)
s.pop()
s.push(45)
s.push(65)
s.push(75)
print(s.size())
print(s.peek())
print(s.is_empty())