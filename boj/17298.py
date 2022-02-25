import sys

n = int(input())
answer = [-1] * n
numbers=list(map(int,input().split()))
stack=[]

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i] :
        answer[stack.pop()]=numbers[i]
    stack.append(i)

print(" ".join(map(str,answer)))

