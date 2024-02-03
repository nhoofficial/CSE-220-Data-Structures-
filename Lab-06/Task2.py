#task2
def insertion_sort(a,i):
    if i==len(a):
        return a
    else:
        for j in range(i-1,-1,-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j]=a[j+1]
                a[j+1]=temp
        return insertion_sort(a,i+1)
arr=[12,65,48,75,46,99,44,33]
print(insertion_sort(arr,0))

#task2



