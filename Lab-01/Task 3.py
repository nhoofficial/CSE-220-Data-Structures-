#task3
def remove(source,size,idx):
    for i in range(idx,size):#idx=2,3,4
        source[i]=source[i+1]#source[2]=40,source[3]=50,
        if i==(size-1):
            source[i]=0#source[4]=0
    print(source)
               
source=[10,20,30,40,50,0,0]
remove(source,5,2)


