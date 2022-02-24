string = input()
result =[]
for i in string:
    if 'A'<= i <='M' or 'a'<=i<='m':
        result.append(chr(ord(i)+13))
    elif 'N'<= i <='Z' or 'n'<=i<='z':
        result.append(chr(ord(i)-13))
    else :
        result.append(i)

print("".join(result))


