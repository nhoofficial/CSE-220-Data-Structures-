class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next

class MyList:
    def __init__(self,a=None):
        self.head = None
        if a == None:
            self.head = None
            n = Node(None, None)
            self.head = n
        elif isinstance(a, list):
            for i in a:
                n = Node(i, None)
                if self.head == None:
                    self.head = n
                    tail = n
                else:
                    tail.next = n
                    tail = n

        elif isinstance(a, MyList):
            copyTail = None
            n = a.head
            while n != None:
                newNode = Node(n.element, None)
                if (self.head == None):
                    self.head = newNode
                    copyTail = newNode
                else:
                    copyTail.next = newNode
                    copyTail = newNode
                n = n.next
        else:
            print("Wrong datatype passed in the constructor so creating an empty MyList")
            self.head = None
            n = Node(None, None)
            self.head = n
#2(2)
    def showList(self):
        n=self.head
        if n==None:
            print("Empty list")
        else:
            i=self.head
            while i!=None:
                print(i.element)
                i=i.next

#2(3)
    def isEmpty(self):
        n=self.head
        if n==None:
            return True
        else:
            return False
#2(4)
    def clear(self):
        n=self.head
        if n!=None:
            self.head=None
            self.next=None
#2(5,6)
    def insert(self,newElement, index=None):
        if index==None:
            n = self.head
            newNode = Node(newElement, None)
            while n != None:
                if n.element == newElement:
                    print("The key already exist in the list")
                    break
                if n.next == None:
                    prev = n
                n = n.next
            prev.next = newNode
            newNode.next = None
        else:
            n = self.head
            newNode = Node(newElement, None)
            size = 0
            while n is not None:
                size += 1
                n = n.next
            if index < 0 and index > size:
                raise Exception("Invalid index")
            if index == 0:
                if self.head == newElement:
                    print("The key already exist in the list")

                else:
                    newNode.next = self.head
                    self.head = newNode
            else:
                if index == size:
                    n = self.head
                    while n != None:
                        if n.element == newElement:
                            print("The key already exist in the list")
                            break
                        if n.next == None:
                            prev = n
                        n = n.next
                    prev.next = newNode
                    newNode.next = None
                else:
                    w = self.head
                    while w != None:
                        if w.element == newElement:
                            print("The key already exist in the list")
                            break
                        w = w.next
                    c = 0
                    n = self.head
                    while c <= size - 1:
                        if c == index - 1:
                            prev = n
                        c += 1
                        n = n.next
                    newNode.next = prev.next
                    prev.next = newNode

#2(7)
    def remove(self, index):
        removedNode=None
        n = self.head
        size = 0
        while n is not None:
            size += 1
            n = n.next
        if (index < 0 or index > size):
            raise Exception("Invalid index")
        if (index == 0):
            removedNode = self.head
            self.head = self.head.next
        else:
            n = self.head
            if index == (size - 1):
                c = 0
                while c <= size - 1:
                    if c == (size - 1) - 1:
                        prev = n
                    if c == size - 1:
                        up = n
                    n = n.next
                    c += 1
                prev.next = up.next
                return up.element
            else:
                c = 0
                while c <= size - 1:
                    if c == index - 1:
                        prev = n
                    if c == index:
                        up = n
                    c += 1
                    n = n.next
                prev.next = up.next
                return up.element

#3(1)
    def evenchecker(self):
        self.copyhead = None
        self.copytail = None
        n = self.head
        while n!=None:
            if n.element%2==0:
                newNode = Node(n.element, None)
                if (self.copyhead == None):
                    self.copyhead = newNode
                    self.copytail = newNode
                else:
                    self.copytail.next = newNode
                    self.copytail = newNode
            n = n.next
        b=self.copyhead
        while b!=None:
            print(b.element,"-",b)
            b=b.next


#3(2)
    def find(self, x):
        n = self.head
        c = 0
        while n != None:
            if n.element == x:
                c += 1
            n = n.next
        if c > 0:
            return True
        else:
            return False
#3(3)
    def reverseList(self):
        prev = None
        n = self.head
        while n!=None:
            nextNode = n.next
            n.next = prev
            prev = n
            n = nextNode
        self.head=prev
#3(4)
    def sortList(self):
        n = self.head
        while (n != None):
            i = n.next
            while (i != None):
                if n.element > i.element:
                    temp=n.element
                    n.element = i.element
                    i.element = temp
                i = i.next
            n = n.next
#3(5)
    def sum(self):
        s = 0
        n = self.head
        while n != None:
            s += n.element
            n = n.next
        print(s)
#3(6)
    def rotate(self,side,k):
        size=0
        n=self.head
        while n!=None:
            size+=1
            n=n.next
        if side=="left":
            a = self.head
            c = 1
            while c <= k:
                temp = self.head
                self.head = self.head.next
                m = 0
                while m < size:
                    if a.next == None:
                        last = a
                        break
                    a = a.next
                last.next = temp
                temp.next = None
                c += 1
        else:
            a=self.head
            c=1
            while c<=k:
                temp = self.head
                m = 0
                while m < size:
                    if m==size-2:
                        last = a
                    else:
                        if a.next==None:
                            end=a
                            break
                    a = a.next
                    m+=1
                self.head=end
                last.next = None
                end.next=temp
                c += 1
lst1 = MyList()
lst2= MyList([2,4,6,1])
#lst3= MyList(lst1)
#lst2.showList()
print(lst2.isEmpty())
#lst2.sortList()
#lst2.insert(1,3)
#lst2.showList()
#lst2.remove(1)
#lst2.showList()
#lst2.evenchecker()
#print(lst2.find(7))
#lst2.reverseList()
#lst2.showList()
#lst2.sum()
lst2.rotate('right',3)
lst2.showList()