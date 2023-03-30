import sys

deque = []


for i in range(0,int(input())):
    command=sys.stdin.readline().split()
    if command[0] == "push_front" :
        deque.insert(0,command[1])

    if command[0] == "push_back" :
        deque.append(command[1])

    if command[0] == "pop_front" :
        if len(deque) != 0 :
            print(deque[0])
            del deque[0]
        elif len(deque) == 0:
            print(-1)

    if command[0] == "pop_back" :
        if len(deque) != 0 :
            print(deque.pop())
        elif len(deque) == 0:
            print(-1)

    if command[0] == "size" :
        print(len(deque))

    if command[0] == "empty" :
        if len(deque) == 0 :
            print(1)
        else :
            print(0)

    if command[0] == "front" :
        if len(deque) != 0:
            print(deque[0])
        elif len(deque) == 0 :
            print(-1)

    if command[0] == "back" :
        if len(deque) != 0:
            print(deque[-1])
        elif len(deque) == 0 :
            print(-1)
