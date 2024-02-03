class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
    def printnode(self):
        print(self.element,"-",self.next)
array=[10,20,30,40,50]
def createlist(array):
    head = None
    tail = None
    for i in array:
        newNode = Node(i, None)
        if(head == None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
def getNode():
    n=createlist(array)
    while n!=None:
        print(n.element)
        n=n.next
getNode()
def copylist(head):
    copyhead=None
    copytail=None
    n=head
    while n is not None:
        newnode=Node(n.element,None)
        if copyhead==None:
            copyhead=None
            copytail=None
        else:
            copytail.next=newnode
            copytail=newnode
    return copyhead
a=createlist(array)
print(copylist(a))
