import sys

oper =list(input())
stack=[]
res=[]
prior={"/":2,"*":2,"+":1,"-":1,"(":0}

for i in range(len(oper)):
    if 'A' <= oper[i] <= 'Z' :
        res.append(oper[i])

    elif oper[i] == '(' :
        stack.append(oper[i])
    
    elif oper[i] == ')':
        while True:
            temp=stack.pop()
            if temp =='(':
                break
            res.append(temp)
        
    else :
        while stack and prior[stack[-1]] >= prior[oper[i]]:
            res.append(stack.pop())
        stack.append(oper[i])

while stack:
    res.append(stack.pop())

print("".join(res))