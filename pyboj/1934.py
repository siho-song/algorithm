
import sys

n=int(sys.stdin.readline())

def lcm(num1, num2):
    cnt =1
    while(1):
        result =num1*cnt
        if(result%num2 ==0):
            return result
        cnt+=1
        
        
for i in range(n):
    num1,num2 = map(int,sys.stdin.readline().split())
    print(lcm(num1,num2))