import sys

nums = list(map(int,sys.stdin.readline().split()))

def lcm(num1, num2):
    cnt =1
    while(1):
        result =num1*cnt
        if(result%num2 ==0):
            return result
        cnt+=1


    
def gcd(num1, num2):
    
    bigNum =0
    smallNum=0
    result=1
    if(num1>num2):
        bigNum=num1
        smallNum=num2
    else:
        bigNum=num2
        smallNum=num1
    
    i=2
    while(i<=smallNum):
       if(smallNum%i ==0 and bigNum%i ==0):
           result=i
       i+=1
    
    return result

print(gcd(nums[0],nums[1]))
print(lcm(nums[0],nums[1]))


    
    