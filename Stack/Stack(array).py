class Stack:
    stack=[]
    size=0
    def push(self,element):#append new element
        self.stack.append(element)
        self.size+=1
    def peek(self):#find the last element in the list
        return self.stack[self.size-1]
    def pop(self):#remove the last element from the list and return the deleted element
        val = self.stack[self.size - 1]
        self.stack[self.size - 1] = None
        self.size -= 1
        return val
h=Stack()
h.push(10)
print(h.peek())
h.push(20)
h.push(30)
print(h.pop())