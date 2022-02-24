numbers = list(map(int,(input().split())))
result=0
i=0
while i<len(numbers):
    digit=len(str(numbers[i+1]))
    result+=(numbers[i]*(10**digit)+numbers[i+1])
    i+=2

print(result)
#자릿수 확인해줘야함

#처음수랑 두번째수 자리 더한거 만큼 10의 n승으로 곱해줘야함 

