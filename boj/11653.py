import sys
import time

#1 

MAX_NUM = 10000000
prime = [False,False]+[True]*(MAX_NUM-1)
m= int(MAX_NUM ** 0.5)
for i in range(1,m+1):
    if prime[i] == True:
        for j in range(i+i,MAX_NUM,i):
            prime[j] = False
primelist = [i for i in range(0,MAX_NUM) if prime[i]==True]
number = int(sys.stdin.readline())
start = time.time()
i=1
while number != 1:
    if number % 2 ==0 :
        print(2)
        number //= 2
    
    else :
        if number % primelist[i] != 0 :
            i+=1
        else :
            number //= primelist[i]
            print(primelist[i])
            i=0
end = time.time()
print(f"{end - start:.5f} sec")
        
#2
number = int(sys.stdin.readline())
start = time.time()
i=2
while number != 1:
    if number % i ==0 :
        print(i)
        number //= i
    
    else :
        i+=1
end = time.time()
print(f"{end - start:.5f} sec")