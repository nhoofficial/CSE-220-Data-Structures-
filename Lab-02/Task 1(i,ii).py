class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
class MyList:
    def __int__(self,a):
        self.head=None
        tail=None
        for i in a:
            n=Node(i,None)
            if self.head==None:
                self.head=n
                tail=n
            else:
                tail.next=n
                tail=n


