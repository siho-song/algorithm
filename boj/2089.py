def func(num):
    a = num // -2
    b= num % -2
    if num==0:
        return '0'
    else:
        if b==0 :
            return func(a) + '0'
        else :
            return func(a+1) + '1'
            

num = int(input())
ans=func(num)
if ans == '0':
    print(ans)
else:
    print(ans[1:])
