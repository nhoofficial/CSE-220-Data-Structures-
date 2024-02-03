a=[10,20,30,40,50]
def RightRotate(a):
    temp=a[-1]
    b=a.copy()#[10,20,30,40,50]
    for i in range(1,len(b)):
        a[i]=b[i-1]
    a[0]=temp
    print(a)
RightRotate(a)    
