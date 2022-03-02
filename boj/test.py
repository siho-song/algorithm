import sys
number = int(sys.stdin.readline())
i=2
while number != 1:
    if number % i ==0 :
        print(i)
        number //= i
    
    else :
        i+=1