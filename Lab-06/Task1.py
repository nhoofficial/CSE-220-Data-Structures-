#task1
def selection_sort(a,i):
    if i==-1:
        return a
    else:
        max = a[i]
        max_idx = i
        for j in range(0, i):
            if a[j] > max:
                max = a[j]
                max_idx = j
        temp = a[i]
        a[i] = max
        a[max_idx] = temp
        return selection_sort(a,i-1)
arr=[12,65,48,75,46,99,44,33]
print(selection_sort(arr,(len(arr)-1)))

#task2



