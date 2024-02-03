#task 7
def max_occ(lst):
    dic={}
    for i in lst:
        dic[i]=0
    for i in dic:
        for j in lst:
            if i==j:
                dic[i]+=1           
    idx=0
    for i in dic:
        if dic[i]>idx:
            idx=dic[i]
    x=None        
    for i in dic:
        if dic[i]==idx:
            x=i
            break

    n=0
    newlst=[]        
    for i in lst:
        if i==x:
            n+=1
        else:
            if i!=x:
                newlst.append(n)      
                n=0
       
    newlst.append(n)        
    hc=0
    for i in range(len(newlst)):
        if newlst[i]>hc:
            hc=newlst[i]
    return hc
        
lst=[1,1,2, 2, 1, 1,1,1]
a=max_occ(lst)
print(a)

