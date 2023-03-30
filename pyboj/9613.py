def gcd(num1,num2):  
    while num2 != 0 :
        num1= num1%num2
        num1 , num2 = num2 , num1
        
    return num1
        

t = int(input())

for i in range(0,t):
    numberlist = list(map(int,(input().split())))
    result=0
    for j in range(1,len(numberlist)-1):
        for k in range(j+1,len(numberlist)):
            if (numberlist[j]>numberlist[k]):
                result += gcd(numberlist[k],numberlist[j])
            else :
                result += gcd(numberlist[j],numberlist[k])            
    print(result)
    
    
 