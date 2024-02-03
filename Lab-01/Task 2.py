#task2
def rotateLeft(source,k):
    new_lst=[0]*len(source)#[0,0,0,0,0,0]
    for i in range(len(source)):  
        if i+k==(len(source)):
            break
        else:
            new_lst[i]=source[i+k]
    c=0        
    for i in range((len(source))-k,len(source)):#6-3,6
        new_lst[i]=source[c]
        c+=1
    return new_lst

source=[10,20,30,40,50,60]
a=rotateLeft(source,3)
print(a)
