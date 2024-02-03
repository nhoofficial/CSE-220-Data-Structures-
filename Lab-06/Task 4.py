#task 4
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

    def selection_sort(self):
        n=self.head
        while n!=None:
            a=self.head
            max=n.element
            max_node=n
            while a!=n:
                if a.element > max:
                    max=a.element
                    max_node=a
                    temp = n.element
                    n.element = max
                    max_node.element = temp
                a=a.next
            n=n.next


a=List()
a.insert([45,23,71,1,36,22])
a.selection_sort()
a.showList()
