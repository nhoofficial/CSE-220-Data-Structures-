#task8
def repition(a):
    dic = {}
    for i in a:
        dic[i] = 0
    for i in dic:
        for j in a:
            if i == j:
                dic[i] += 1
    sup = 0
    for i in dic:
        if dic[i] > sup:
            sup = dic[i]
    c = 0
    for i in dic:
        if dic[i] == sup:
            c += 1
    if c >= 2:
        return True
    else:
        return False
a = [3,4,6,3,4,7,4,6,8,6,6]
rep=repition(a)
print(rep)