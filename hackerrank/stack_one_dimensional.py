class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return  self.stack[-1]

    def sizeStack(self):
        return len(self.stack)




stack = Stack()
stack.push(1)
stack.push(2)
stack.push(25)
stack.push(34)
stack.pop()
print stack.stack
stack.sizeStack()
