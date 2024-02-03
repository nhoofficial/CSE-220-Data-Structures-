class Queue:
    size=0
    start=0
    arr=[0]*5
    def enqueue(self,data):
        if self.size==len(self.arr):
            print("No more space left inside the array :)")
        else:
            self.arr[(self.start + self.size) % len(self.arr)] = data #we'll do that for the circular array cz if we use size then it'll work like linear concept.
            self.size += 1
    def dequeue(self):
        val=self.arr[self.start]
        self.size-=1
        self.arr[self.start]=None
        self.start=(self.start+1)%len(self.arr)
        return val
    def peek(self):
        return self.arr[self.start]
a=Queue()
a.enqueue(10)
a.enqueue(20)
print(a.peek())
a.enqueue(30)
a.enqueue(40)
a.enqueue(50)
a.enqueue(60)

