#1번코드
import sys
number= list(sys.stdin.readline().rstrip())
result =0
iter=len(number)

for i in range(0,len(number)):
    if number[i] == '1':
        a,b=divmod((iter-1)-i,3)
        result += ((2**b)*(10**a))

print(result)


# 2번코드
import sys

n = list(sys.stdin.readline().rstrip())
res = []
for i in range(len(n)):
    n[i] = int(n[i])

n = n[::-1]

tmp = 0
for i in range(len(n)):

    tmp += n[i]*(2**(i%3))
    if (i % 3 == 2 and i != 0) or i == (len(n) - 1):
        res.append(str(tmp))
        tmp = 0

res = res[::-1]
print("".join(res))

#3번코드

print(oct(int(input(),2))[2:])