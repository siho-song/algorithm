def gcd(num1,num2):   
    while num2 != 0:   
        num1 = num1 % num2 
        num1,num2 = num2 ,num1
    return num1

N,S = map(int,(input().split())) 

brolocation = list(map(int,(input().split())))

pos =[abs(S-i) for i in brolocation]
ans = 1000000000
if len(pos) == 1: 
    print(pos[0]) 
    
else :
    for i in range(0,len(pos)-1):
        num=gcd(pos[i],pos[i+1])
        if ans > num :
            ans = num
            
print(ans)


