def linear_search(a,val):
    for i in range(len(a)):
        if a[i] == val:
            return i
    return -1
a=[12,13,14,2]
print(linear_search(a,0))

#for doing the binary search operation at first we have to sort the array.
arr=[21,56,48,75,64,12]
for i in range(len(arr)-1,-1,-1):
    for j in range(0,i):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
def binary_search(arr,val):
    l=0
    r=len(arr)-1
    while (l<=r):
        m=(l+r)//2
        if arr[m] == val:
            return m
        else:
            if arr[m]<val:
                l=m+1
            else:
                r=m-1
    return -1
print(binary_search(arr,69))