class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
    def printnode(self):
        print(self.element,"-",self.next)
n4=Node(40,None)
n3=Node(30,n4)
n2=Node(20,n3)
n1=Node(10,n2)
head=n1
def copyNode(head):
    copyhead=None
    copytail=None
    n=head
    while n!=None:
       newNode=Node(n.element,None)
       if copyhead==None:
           copyhead=newNode
           copytail=newNode
       else:
           copytail.next=newNode
           copytail=newNode
       n=n.next
    return copyhead
def getNode(head):
    a=reverseList(head)
    n=a
    while n!=None:
        print(n.element)
        n=n.next
def reverseList(head):

    copyHead = None

    n = head

    while(n is not None):

        newNode = Node(n.element, None)

        if(copyHead == None):

            copyHead = newNode

        else:

            newNode.next = copyHead

            copyHead = newNode

        n = n.next

    return copyHead
getNode(head)