import sys
N=int(sys.stdin.readline())
fac=[1,1]+[0]*10

for i in range(2,len(fac)) :
    if fac[i] == 0 :
        fac[i] = fac[i-1] * i
num1=1
num2=2
num3=3
                
for i in range(0,N):
    num = int(sys.stdin.readline())
    answer=0
    for j in range(0, num+1//1):
        for p in range(0,num//2+1):
                for r in range(0,num//3+1):
                    if num1*j+num2*p+num3*r == num :
                        answer += fac[j+p+r] // (fac[j]*fac[p]*fac[r])
    print(answer)

