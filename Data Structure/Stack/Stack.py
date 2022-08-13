class Stack:
    def __init__(self):
        self._stack = []
        self.length = 0
    def push(self,x)->None:
        self._stack.append(x)
        self.length +=1
    def pop(self)->int:
        if self.isEmpty():
            return -1
        item = self._stack.pop()
        self.length -=1
        return item
    def isEmpty(self)->bool:
        return len(self._stack)==0
    
if __name__=="__main__":
    stack = Stack()
    stack.push("Gunjan")
    stack.push("Paul")
    print(stack.pop())