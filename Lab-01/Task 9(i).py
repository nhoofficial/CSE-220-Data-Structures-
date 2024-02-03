#circular array
#1
source=list(map(int,input().rstrip().split(",")))
size=int(input())
start=int(input())
def palindrome(source,start,size):
    lst=[0]*len(source)
    c=(start+(size-1))%len(source)
    for i in range(size):
        lst[start]=source[c]
        c=(c-1)%len(source)
        start=(start+1)%len(source)
    if lst==source:
        return True
    else:
        return False
c=palindrome(source,start,size)
print(c)