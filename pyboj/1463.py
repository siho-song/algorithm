import sys

number = int(sys.stdin.readline())
minimum =[0,0,1,1]+[0]*(number-3)
answer =0

for i in range(2,number+1):
    minimum[i]=minimum[i-1]+1
    if i % 2 ==0:
        minimum[i] = min(minimum[i],minimum[i//2]+1) 
    if i%3 == 0:
        minimum[i] = min(minimum[i],minimum[i//3]+1)
        
print(minimum[number])
        
