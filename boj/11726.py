import sys

# def factorial(num):
#     if num == 1 :
#         return 1
#     temp= num -1
#     return num * factorial(temp)

fac=[1,1]+[0]*999

for i in range(2,len(fac)) :
    if fac[i] == 0 :
        fac[i] = fac[i-1] * i
        
answer = 1
num = int(sys.stdin.readline())

if num==1 :
    answer =1  
for i in range(2,num+1,2) :
    answer += ((fac[(num-i)+(i//2)]) // (fac[num-i]*fac[i//2])) 

print(answer%10007)