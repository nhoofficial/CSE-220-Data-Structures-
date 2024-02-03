class Node:
    def __init__(self,element,next,prev):
        self.element=element
        self.next=next
        self.prev=prev
class Queue:
    head = Node(None, None, None)
    head.next = head.prev = head
    tail=None
    def enqueue(self,data):
        newNode=Node(data,None,None)
        if self.head.next == self.head:
            self.head.next = newNode
            newNode.prev = self.head
            newNode.next = self.head
            self.head.prev = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            newNode.next = self.head
            self.head.prev = newNode
            self.tail = newNode
    def dequeue(self):
        val=self.head.next.element
        temp=self.head.next
        self.head.next=temp.next
        temp.next.prev=self.head
        temp.elment=None
        temp.next=None
        return val
    def peek(self):
        return self.head.next.element
a=Queue()
a.enqueue(10)
a.enqueue(20)
print(a.peek())
a.dequeue()
print(a.peek())

