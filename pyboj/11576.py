import sys

A,B=map(int,sys.stdin.readline().split())

m= int(sys.stdin.readline())
num = list(map(int,(sys.stdin.readline().rsplit())))
result = 0
ans=[]
for i in range(0,m):
    num[i] *= A**(m-(i+1)) 
    result+=num[i]

while result != 0:
    num1,num2 = divmod(result,B)
    result = num1
    ans.append(num2) 
    
print(" ".join(map(str,ans[::-1])))

