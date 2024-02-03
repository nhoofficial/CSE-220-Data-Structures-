class Node:
    def __init__(self,element):
        self.element=element
        self.next=None
class Stack:
    head=None
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            n=Node(data)
            n.next=self.head
            self.head=n
    def peek(self):
        return self.head.element
    def pop(self):
        a=self.head
        self.head=self.head.next
        a.element=None
        a.next=None
b=Stack()
b.push(10)
print(b.peek())