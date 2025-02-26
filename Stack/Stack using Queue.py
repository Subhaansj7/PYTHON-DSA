from queue import Queue 

class Stack:
    def __init__(self):
        self.q = Queue()
        
    def push(self,x):
        s = self.q.qsize()
        self.q.put(x)
        for i in range(s):
            self.q.put(self.q.get())
    
    def pop(self):
        n = self.q.get()
        return n 
    
    def top(self):
        return self.q.queue[0]
        
    def size(self):
        return self.q.qsize()
        
#driver 

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(4)
    s.push(1)
    print("Top of the stack: ", s.top())
    print("Size of the stack before removing element: ", s.size())
    print("The deleted element is: ", s.pop())
    print("Top of the stack after removing element: ", s.top())
    print("Size of the stack after removing element: ", s.size())