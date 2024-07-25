from queue import LifoQueue
#LifoQueue is a Stack in python

class Queue:
    def __init__(self):
        self.input = LifoQueue()
        self.output = LifoQueue()
        
    def push(self,data):
        #Pop all the elements from stack input 
        while not self.input.empty():
            self.output.put(self.input.get())
        #Insert desired elements in  stack input 
        print("element pushed is ,",data)
        self.input.put(data)
        #Pop elements from the stack output
        #and push them into stack input 
        while not self.output.empty():
            self.input.put(self.output.get())
    
    def pop(self):
        if self.input.qsize()==0:
            print("Stack is empty")
            exit(0)
        val = self.input.get()
        return val 
    
    def Top(self):
        if self.input.qsize()==0:
            print("stack is empty")
            exit(0)
        return self.input.queue[-1]
        
    def size(self):
        return self.input.qsize()
        
#driver 
if __name__ == "__main__":
    q = Queue()
    q.push(3)
    q.push(4)
    print("The element poped is", q.pop())
    q.push(5)
    print("The top of the queue is", q.Top())
    print("The size of the queue is", q.size())