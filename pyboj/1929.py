def is_prime(num1,num2):
    primelist = [True]*(num2+1)
    primelist[0] = False
    primelist[1] = False
    m= int(num2**0.5)
    for i in range(2,m+1):
        if primelist[i] == True:
            for j in range(i+i,num2+1,i):
                primelist[j] = False
                
    return [i for i in range(num1,num2+1) if primelist[i]== True]
                
number1 , number2 = map(int,input().split())

primelist = is_prime(number1,number2)

for i in primelist:
    print(i)