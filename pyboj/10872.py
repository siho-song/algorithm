number = int(input())
result =1
if number == 0 :
    print(result)
else :
    for i in range(2,number+1):
        result *= i
    print(result)
        
