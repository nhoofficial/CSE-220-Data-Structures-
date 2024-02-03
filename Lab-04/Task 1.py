
class Stack:
    size=0
    arr=[None]*(100)
    def push(self,data):
        if len(self.arr)==self.size:
            print("Stack overflow")
        else:
            self.arr[self.size]=data
            self.size+=1
    def pop(self):
        reval=self.arr[self.size-1]
        self.arr[self.size-1]=None
        self.size-=1
        return reval
    def peek(self):
        if self.size==0:
            return None
        else:
            return self.arr[self.size-1]
a=Stack()
s=input("Enter the equation: ")
c=0
cnt=0
num=1
for i in range(len(s)):
    if s[i] == "{" or s[i]=='[' or s[i]=='(' :
        a.push(s[i])
        c+=1
        num+=1
    else:
        if s[i]==')' or s[i]=='}' or s[i]==']':
            string=""
            f=a.peek()
            num+=1
            if f!=None:
                string = f + s[i]
                if string == '{}' or string == '[]' or string == '()':
                    cnt += 1
                    a.pop()
            else:
                if f==None:
                    print("This expression is not correct.")
                    print("Error at character #" + str(i+1) + "." + s[i] + " - not opened")
                    cnt-=1
                    break
                else:
                    cnt-=1
                    break
if c==cnt:
    print("This expression is correct")
else:
    if a.peek() != None:
        print("This expression is not correct.")
        print("Error at character #" + str(num) + "." + a.peek() + " - not closed")







