import sys

n = int(sys.stdin.readline())

result = [-1 for i in range(n)]
array= list(map(int,sys.stdin.readline().split()))
stack = []

for i in range(n):
    while stack and (array[stack[-1]]<array[i]):
        result[stack.pop()]=array[i]
    stack.append(i)
        
print(result)


