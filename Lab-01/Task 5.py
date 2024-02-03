#task5
a=list(map(int,input().rstrip().split(",")))
def spilitting(a):
    sum=0
    sum1=0
    for i in range(len(a)):
        sum+=a[i]
    c=sum/2    
    for i in range(len(a)-1):
        if sum1==c:
            i=len(a)-2
        else:
            sum1+=float(a[i])
    if sum1==c:
        print('True')
    else:
        print('False')
spilitting(a)    

