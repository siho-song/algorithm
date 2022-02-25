from collections import Counter

n = int(input())
numbers = list(map(int,input().split()))
frequency=Counter(numbers)
stack=[]
answer=[-1]*n

for i in range(n):
    while stack and frequency[numbers[stack[-1]]] < frequency[numbers[i]] :
        answer[stack.pop()] = numbers[i]

    stack.append(i)

print(*answer)
