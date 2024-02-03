a=[10,20,30,40,50,0,0,0]
def shifting(a,size):
    if size==len(a):
        print('No space for shifting')
    i=size-1
    while i>=0:
        a[i+1]=a[i]
        i-=1
    a[0]=0
    print(a)
shifting(a,5)    
    
    