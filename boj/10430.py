numbers=list(map(int,(input().split())))

print((numbers[0]+numbers[1])%numbers[2])
print(((numbers[0]%numbers[2])+(numbers[1]%numbers[2]))%numbers[2])
print((numbers[0]*numbers[1])%numbers[2])
print(((numbers[0]%numbers[2]) * (numbers[1]%numbers[2]))%numbers[2])