import sys

strlist =[]
templist =[]
bucket=list(input())
j=0
while j < len(bucket) :
    if bucket[j] == '<' :
        while bucket[j] != '>' :
            templist.append(bucket[j])
            j += 1
        if bucket[j] == '>':
            templist.append(bucket[j])
            j+=1
        strlist.append("".join(map(str,templist)))
        templist =[]

    elif bucket[j] == ' ':
        templist.append(bucket[j])
        j += 1
        strlist.append("".join(map(str,templist)))
        templist =[]

    else :
        while bucket[j] != " " and bucket[j] != "<":
            templist.append(bucket[j])
            j += 1
            if j==len(bucket):
                break
        templist.reverse()
        strlist.append("".join(map(str,templist)))
        templist =[]

print("".join(map(str,strlist)), sep='')

