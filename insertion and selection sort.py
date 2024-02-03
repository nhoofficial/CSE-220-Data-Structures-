

a=[4,3,5,2,9,0]
i=len(a)-1
def recursive_sort(a,i):
    if i==-1:
        return a
    max = i
    max_idx = i
    for j in range(i):
        if a[j] > max:
            max = a[j]
            max_idx = j
    temp = a[max_idx]
    a[max_idx] = a[i]
    a[i] = temp
    return recursive_sort(a,i-1)
#print(recursive_sort(a,i))

def insertion_sort(a,i):
    if i == len(a):
        return a
    for j in range(i-1,-1,-1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j]=a[j+1]
            a[j+1]=temp
        else:
            break
    return insertion_sort(a, i+1)
print(insertion_sort(a,0))