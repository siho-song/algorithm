def is_prime(n):
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if  n%i == 0:
            return False
    return True    
        
num = int(input())
numbers = list(map(int,input().split()))
result =0

for i in numbers :
    if i == 1 : 
        continue
      
    elif is_prime(i):
        result+=1
        
print(result)
        
'''
def prime_list(n):
    # 에라토스테네스의 체 초기화 : n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n
    
    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n,i):
                sieve[j] = False
    
    return [i for i in range(2,n) if sieve[i]==True]
'''