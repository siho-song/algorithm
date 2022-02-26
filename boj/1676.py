number = int(input())

result =1
for i in range(2,number+1):
    result *= i

i=1
cnt =0
while True:    
    
    if str(result)[-i] == '0' :
        cnt+=1
        i+=1
    else : break
    
print(cnt)
        