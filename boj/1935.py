n = int(input())
word = input()
num_lst=[0]*n
stack=[]
result=[]

for i in range(n):
    num_lst[i]=int(input())
    
for i in word:
    if 'A' <= i <= 'Z':
        stack.append(num_lst[ord(i)-ord('A')])
    
    else :
        num2=stack.pop()
        num1=stack.pop()
        if i == '+':
            stack.append(num1+num2)
        
        elif i == '-':
            stack.append(num1-num2)
        
        elif i == '*':
            stack.append(num1*num2)
        
        elif i == '/':
            stack.append(num1/num2)


print('%.2f' %stack[0])


