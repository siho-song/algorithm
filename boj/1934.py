import math
num = int(input())

for i in range(num):
    a,b = map(int,input().split())
    result=a*b/math.gcd(a,b)
    print(int(result))
    