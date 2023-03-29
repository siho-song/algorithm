import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
result = [-1 for i in range(n)]
cnt_table = [0 for i in range(10000001)]
for i in array:
    cnt_table[i]+=1
    
stack =[0]

for i in range(1,n):
    
    while(stack and cnt_table[array[i]]>cnt_table[array[stack[-1]]]):
        result[stack.pop()]=array[i]
    
    stack.append(i)
    

print(*result)
