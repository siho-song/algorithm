"""def is_prime(num):
    m = int(num ** 0.5)
    for i in range(2,m+1):
        if num % i ==0 :
            return False
    return True
"""
def prime_list(num):
    primelist = [True] * num
    primelist[0]=False
    primelist[1]=False
    m= int(num ** 0.5)
    for i in range(2,m+1):
        if primelist[i] == True:
            for j in range(i+i,num,i):
                primelist[j] == False
    return [i for i in range(i,len(primelist),2) if primelist[i]==True]        
    
while True:
    num = int(input())
    if num == 0 :
        break
    
    primelist = prime_list(num)
    
    while True:
        if num - 
        
    
    