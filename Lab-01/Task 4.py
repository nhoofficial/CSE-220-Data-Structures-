#task4
def removeAll(source,size,element):
    lst=[]
    for i in range(size):
        if source[i]!=element:
            lst.append(source[i])
    lst=[10,30,50]        
    c=len(source)-len(lst) #9-3=6  
    for i in range(c):
        lst.append(0)
    source=lst
    print(source)
    
        
        
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
