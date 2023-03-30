import sys
cardnum = int(sys.stdin.readline())

cardlist = [0]+list(map(int,sys.stdin.readline().rsplit()))

maxlist = cardlist

for i in range(1,cardnum+1):
    for j in range(0,i//2+1):
        maxlist[i] = max(maxlist[i],maxlist[i-j]+maxlist[j])


print(maxlist[cardnum])



