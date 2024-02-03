#task 3
class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
class List:
    head=None
    def insert(self,a):
        tail=None
        for i in a:
            newNode=Node(i,None)
            if self.head == None:
                self.head=newNode
                tail=newNode
            else:
                tail.next=newNode
                tail=newNode
        tail.next=None
    def showList(self):
        n=self.head
        while n!=None:
            print(n.element)
            n=n.next
    def bubble_sort(self):
        n=self.head
        while n!=None:
            a=self.head
            while a!=n:
                if a.element > n.element:
                    temp = a.element
                    a.element = n.element
                    n.element = temp
                a=a.next
            n=n.next
a=List()
a.insert([14,56,28,42,140])
a.bubble_sort()
a.showList()
