import sys

while True:

    line=sys.stdin.readline().rstrip("\n")
    
    if not line :
        break
    
    up,lo,di,space = 0 ,0 ,0,0
    for i in line:
        if i.islower() :
            lo +=1
        elif i.isupper():
            up +=1
        
        elif i.isdigit():
            di+=1
        elif i.isspace():
            space+=1
    print(lo, up, di, space)
