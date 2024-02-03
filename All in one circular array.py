circularArray=[40,50,0,0,0,0,0,0,10,20,30]
def print_forward(start,circularArray,size):
    for i in range(size):
        print(circularArray[start])
        start=(start+1)%len(circularArray)
print_forward(8,circularArray,5)

def print_reverse(c,start,size):
    index=start+size-1
    for i in range(size):
        print(c[index%len(c)])
        index-=1
print_reverse(circularArray,8,5)


a=[10,23,30,40,50,0,0,0,0,0]
def liner_to_circular(a,start,size):
    new=[0]*len(a)
    for i in range(size):
        new[start]=a[i]
        start=(start+1)%len(a)
    return new
print(liner_to_circular(a,8,5))

def resize(start,size,c):
    new=[0]*(size+2)
    resizecirc=start

    for i in range(size):
        new[start] = c[resizecirc]
        start=(start+1)%len(new)
        resizecirc=(resizecirc+1)%len(c)
    return new
a=[20,30,40,50,10]
print(resize(4,5,a))





