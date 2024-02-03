class Keysearch_sort:
    def __init__(self,arr):
        max=min=0
        for i in arr:
            if max<i:
                max=i
            else:
                if min>i:
                    min=i
        self.aux=[0]*(max+1)
        for i in range(0,len(arr)):
            self.aux[arr[i]]=+1
    def search(self,val):
        if self.aux[val]!=0:
            return True
        else:
            return False
    def sort(self):
        array=[]
        for i in range(len(self.aux)):
            if self.aux[i]!=0:
                array.append(i)
        return array
op=[2,4,7,1]
a=Keysearch_sort(op)
print(a.search(5))
print(a.sort())

