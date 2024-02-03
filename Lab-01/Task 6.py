#task 6
def array_series(n):
    lst = []
    for i in range(1, n + 1):  # n=2:{0,1,2,1 }
        for zero in range(0, n - i):  # 2-1=1
            lst.append(0)
        for num in range(i, 0, -1):
            lst.append(num)
    return lst
n = int(input())
a=array_series(n)
print(a)
