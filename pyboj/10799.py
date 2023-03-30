import sys
tempstack = list(input())
stack =[]
count = 0
result = 0
i=0

while i < len(tempstack) :
    if tempstack[i] == '(' :
        count+=1
        i+=1

    elif tempstack[i-1] == '(' and tempstack[i] == ')' :
        i+=1
        count -=1
        result += count
    
    elif tempstack[i-1] == ')' and tempstack[i] ==')' :
        i+=1
        count -=1
        result +=1

print(result)


