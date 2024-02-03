source1=[40,50,0,0,0,10,20,30]
source2=[10,20,5,0,0,0,0,0,5,40,15,25]
def intersection(source1,start_1,size_1,source2,start_2,size_2):
    new_lst1=[]
    new_lst2=[]
    cmn=[]
    for i in range(size_1):
        new_lst1.append(source1[start_1])
        start_1=(start_1+1)%len(source1)
        
    for i in range(size_2):
        new_lst2.append(source2[start_2])
        start_2=(start_2+1)%len(source2)
        
    if len(new_lst1)>len(new_lst2):
        for i in range(len(new_lst2)):
            for j in range(len(new_lst1)):
                if new_lst2[i] in new_lst1:
                    if new_lst1[i] not in cmn:
                            cmn.append(new_lst1[i])
    else:
        if len(new_lst2)>len(new_lst1):
            for i in range(len(new_lst1)):    
                for j in range(len(new_lst2)):
                    if new_lst1[i] in new_lst2:
                        if new_lst1[i] not in cmn:
                            cmn.append(new_lst1[i]) 
        else:
            for i in range(len(new_lst1)):
                for j in range(len(new_lst1)):
                    if new_lst1[i] in new_lst2:
                        if new_lst1[i] not in cmn:
                            cmn.append(new_lst1[i])
    return cmn
common=intersection(source1,5,5,source2,8,7)    
print(common)               
                