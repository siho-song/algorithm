import sys
import time

T = int(sys.stdin.readline())

def Primelist(num):
    prime=[True]*(num+1)
    prime[0]=False
    prime[1]=False
    m= int(num**0.5)
    for i in range(2,m+1):
        if prime[i] == True:
            for j in range(i+i,num+1,i):
                prime[j]=False
    return prime

num = [int(sys.stdin.readline()) for i in range(0,T)]

m= max(num)
prime=Primelist(m)

    
for i in num:
    # start = time.time()
    result =0
    for j in range(0,i//2+1):
        if prime[j] and prime[i-j] :
            result +=1
    print(result)
    # end = time.time()
    # print(f"{end - start:.5f} sec")
