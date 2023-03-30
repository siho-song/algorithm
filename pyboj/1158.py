import sys
queue = []
printlist=[]
command=list(map(int,input().split()))
delpoint = -1
for i in range(1,command[0]+1):
    queue.append(i)

#queue = [i for i in range(1,command[0]+1)]

for i in range(0,command[0]):
    delpoint += command[1]
    if delpoint>=len(queue) :
        delpoint = delpoint % len(queue)
    printlist.append(queue.pop(delpoint))
    delpoint -=1

print("<",", ".join(map(str,printlist)),">", sep='')


