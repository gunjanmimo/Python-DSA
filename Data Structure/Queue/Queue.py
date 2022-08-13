# %%
class Queue:
    def __init__(self) -> None:
        self.queue = []
        self.length = 0
    
    def enqueue(self,x):
        self.length+=1
        self.queue = [x]+self.queue
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        self.length -=1
        return self.queue.pop()

    def isEmpty(self):
        return self.queue==0
    
    def size(self):
        return self.length

# %%
if __name__=="__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(100)
    queue.enqueue(1000)
    print(queue.size())
    print(queue.dequeue())
# %%
