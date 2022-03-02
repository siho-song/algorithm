import sys

stacklist = []

def push(a):
    stacklist.append(a)

def pop():
    if empty()==0:
        print(stacklist[-1])
        stacklist.pop()
    else : print(-1)


def size():
    size = len(stacklist)
    print(size)

def empty():
    if len(stacklist)==0:
        return 1
    else: return 0

def top():
    if empty()==0:
        print(stacklist[-1])
    else : print(-1)



number = int(sys.stdin.readline())

for i in range(number) :
    command = sys.stdin.readline().split()

    if command[0] == 'push' :
        push(command[1])
    elif command[0] =='top':
        top()
    elif command[0] =='size':
        size()
    elif command[0]  == 'empty':
        print(empty())
    elif command[0]  == 'pop':
        pop()

