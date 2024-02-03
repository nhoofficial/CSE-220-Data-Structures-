
a=[1,4,5,0,7,2,3]
def bubble_sort(a):

  for i in range(len(a)-1,-1,-1):

    for j in range(0,i):

      if a[j]>a[j+1]:

        temp = a[j]

        a[j]=a[j+1]

        a[j+1]=temp
bubble_sort(a)

A=[12,25,7,45,75,96]


def selection_sort(A):

  max_idx = 0

  max = A[0]

  for i in range(len(A)-1,-1,-1):

    max = A[i]

    max_idx = i

    #finding the maximum value

    for j in range(0,i):

      if(A[j]>max):

        max = A[j]

        max_idx = j

    #swapping

    temp = A[max_idx]

    A[max_idx]=A[i]

    A[i]=temp
  return A
print(selection_sort(A))

b=[5,76,23,45,33]
def insertion_sort(b):
    for i in range(len(b)):
        for j in range(i-1,-1,-1):
            if b[j]>b[j+1]:
                temp=b[j]
                b[j]=b[j+1]
                b[j+1]=temp

    return b
print(insertion_sort(b))
