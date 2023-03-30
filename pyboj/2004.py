def Counter2(num):
    cnt =0
    n = 2
    while True:
        if num >= n :
            cnt += num // n
            n = n *2
        else :
            break
    return cnt
            
def Counter5(num):
    cnt =0
    n = 5
    while True:
        if num >= n :
            cnt += num // n
            
            n = n *5
        else :
            break     
    return cnt     
         

number1,number2 = map(int,input().split())
a=Counter2(number1)-Counter2(number1-number2)-Counter2(number2)
b=Counter5(number1)-Counter5(number1-number2)-Counter5(number2)

if a>=b :
    print(b)

else : print(a)
