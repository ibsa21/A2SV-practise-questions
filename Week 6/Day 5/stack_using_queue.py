class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        pop_number = self.stack2.pop()
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return pop_number

    def peek(self) -> int:
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        peek_number = self.stack2[-1]
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())
        return peek_number
    
    def empty(self) -> bool:
        return self.stack1 == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
