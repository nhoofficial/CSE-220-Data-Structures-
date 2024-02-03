class KeyIndex:
    def __init__(self, arr):
        self.max = self.min = 0
        for i in arr:
            if self.max < i:
                self.max = i
            else:
                if self.min > i:
                    self.min = i
        if self.min < 0:
            self.min *= -1
        self.k = [0] * (self.max + self.min + 1)
        for i in range(0, len(arr)):
            self.k[arr[i] + self.min] = +1

    def search(self, val):
        if val + 1 > len(self.k):
            return False
        else:
            if self.k[val + self.min] != 0:
                return True
            else:
                return False

    def sort(self):
        c = 0
        for i in range(len(self.k)):
            if self.k[i] != 0:
                c += 1
        array = [0] * c
        n = 0
        for i in range(len(self.k)):
            if self.k[i] != 0:
                array[n] = i - self.min
                n += 1
        return array


op = [4,6,8,2,0,-3,5,6,9,-15,5,6,77,9]
a = KeyIndex(op)
print(a.search(-4))
print(a.sort())
