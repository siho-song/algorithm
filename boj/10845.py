import sys
queue = []

for i in range(0,int(sys.stdin.readline())):
    command=sys.stdin.readline().split()
    if command[0] == "push":
        queue.append(command[1])

    elif command[0] == "pop":
        if queue:
            print(queue[0])
            del queue[0]

        elif not queue:
            print("-1")

    elif command[0] == "size":
        print(len(queue))

    elif command[0] == "empty":
        if not queue :
            print("1")
        elif queue :
            print("0")

    elif command[0] == "front":
        if queue :
            print(queue[0])
        elif not queue :
            print("-1")

    elif command[0] == "back":
        if queue :
            print(queue[len(queue)-1])
        elif not queue :
            print("-1")


