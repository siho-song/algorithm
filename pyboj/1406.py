import sys
leftstackary = list(input())
rightstackary=[]  

for i in range(0,int(sys.stdin.readline())):
    command=sys.stdin.readline().split()
    if command[0] == "L":
        if leftstackary :
            rightstackary.append(leftstackary.pop())

    elif command[0] == "D":
        if rightstackary:
            leftstackary.append(rightstackary.pop()) 

    elif command[0] == "B":
        if leftstackary :
            leftstackary.pop()
        
    else:
        leftstackary.append(command[1])

print("".join(leftstackary+list(reversed(rightstackary))))
