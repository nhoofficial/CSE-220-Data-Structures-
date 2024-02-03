#task2
class HashTable:
    def __init__(self,arr):
        self.arr=arr
        self.hashtable=[0]*len(arr)
    def hash(self):
        cons = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.size = len(self.hashtable)
        for i in self.arr:
            c = 0
            dig = 0
            for j in range(len(i)):
                if i[j] in cons:
                    c += 1
                else:
                    if i[j] in num:
                        dig += int(i[j])
            val = ((c * 24) + dig) % len(self.arr)
            if self.hashtable[val]==0:
                self.hashtable[val] = i
            else:
                if self.hashtable[val]!=0:
                    for k in range(0, self.size):
                        val = (val + 1) % len(self.hashtable)
                        if self.hashtable[val] == 0:
                            self.hashtable[val] = i
                            break
        return self.hashtable
lst=['ST1E89B8A32','ABC','DEF32','GJHGF','IOS12','WER98','POWE23','VAIO0','NK78']
A=HashTable(lst)
print(A.hash())


