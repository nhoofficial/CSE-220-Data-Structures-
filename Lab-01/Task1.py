def shiftLeft(source,k):
    new_lst=[0]*len(source)
    for i in range(len(source)):
        new_lst[i]=source[i+k]
        if i+k==len(source)-1:
            new_lst[i]=source[i+k]
            break
    for i in range(i+k,len(source)):
        new_lst[i]=0
    return new_lst
source=[10,20,30,40,50,60]
s=shiftLeft(source,3)
print(s)


