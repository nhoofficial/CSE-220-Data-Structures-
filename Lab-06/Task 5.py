#task5
class Node:
    def __init__(self,element,next,prev):
        self.element=element
        self.next=next
        self.prev=prev
class DoublyList:
    head=None
    def insert(self,a):
        tail=None
        for i in a:
            newNode=Node(i,None,None)
            if self.head == None:
                self.head=newNode
                tail=newNode
            else:
                tail.next=newNode
                newNode.prev=tail
                tail=newNode
        tail.next=None
    def showList(self):
        n=self.head
        while n!=None:
            print(n.element)
            n=n.next

    def insertion_sort(self):
        n=self.head.next
        while n!=None:
            a=n.prev
            while a!=None:
                if a.element > a.next.element:
                    temp = a.next.element
                    a.next.element = a.element
                    a.element = temp
                a=a.prev
            n=n.next

a=DoublyList()
a.insert([12,45,6,2,99,28])
a.insertion_sort()
a.showList()
