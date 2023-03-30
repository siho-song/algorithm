line = input()
cnt =0
for i in line:
    if 'A'<=i<='Z' or 'a'<= i <='z':
        cnt +=1

print(cnt)
