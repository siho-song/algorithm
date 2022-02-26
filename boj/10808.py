alphalist = [-1]*26

string = input()
cnt =0 
for i in string:
    temp = ord(i)-ord("a")
    if alphalist[temp] == -1 :
        alphalist[temp]= cnt
    cnt+=1 

print(" ".join(map(str,alphalist)))