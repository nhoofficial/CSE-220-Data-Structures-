#task6
a=[14,23,26,48,75]
def binary_search(a,val,l,r):
    mid=(l+r)//2
    if l>r:
        return -1
    elif a[mid]==val:
        return mid
    else:
        if a[mid]<val:
            return binary_search(a,val,mid+1,r)
        else:
            return binary_search(a,val,l,mid-1)
print(binary_search(a,75,0,len(a)-1))





