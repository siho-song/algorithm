import sys
stacklist = []
templist = []

def push(a):
    stacklist.append(a)

def pop():
    if empty()==False:
        stacklist.pop()
    else : print("stack is empty")


def size():
    size = len(stacklist)
    print(size)

def empty():
    if len(stacklist)==0:
        return True
    else: return False

def top():
    if empty()==False:
        return stacklist[-1]


number = int(sys.stdin.readline())
inputnum=int(sys.stdin.readline())
for i in range(1,number+1):
    if inputnum != top() :
        stacklist.append(i)
        print(stacklist)

    elif inputnum == top():
        templist.append(top())
        pop()
        print("stacklisk : " , stacklist)
        print("templist : ", templist)
        inputnum=int(sys.stdin.readline())
        print("inputnum : ",inputnum)
        print(" i : ", i)
   

