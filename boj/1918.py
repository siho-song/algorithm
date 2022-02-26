import sys

oper = list(input())
stack =[]
result=[]
prior = {"/":2,"*":2,"+":1,"-":1,"(":0}

for i in range(len(oper)) :
    if  'A' <= oper[i] <= 'Z' :
        result.append(oper[i])
    
    elif oper[i] == '(' :
        stack.append(oper[i])
    
    elif oper[i] == ')' :
        while True:
            temp = stack.pop()
            if temp =='(' :
                break
            result.append(temp)

    else :
        while stack and prior[stack[-1]] >= prior[oper[i]]:
            result.append(stack.pop())
        stack.append(oper[i])

        
while stack:
    result.append(stack.pop())
        
print("".join(result))

