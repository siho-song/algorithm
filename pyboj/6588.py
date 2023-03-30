r=1000000
primelist = [True] * r
m= int(r ** 0.5)
for i in range(2,m+1):
    if primelist[i] == True:
        for j in range(i+i,r,i):
            primelist[j] = False

    
while True:
    num = int(input())
    if num == 0 :
        break
    
    for i in range(3,len(primelist)): 
        if primelist[i]==True and primelist[num-i]==True:
            print(num,"=",i,'+',num-i)
            break        
        
    
    