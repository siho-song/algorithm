string = input()
strlist =[]
for i in range(len(string)):
    strlist.append(string[i:])
strlist.sort()

for i in strlist:
    print(i)