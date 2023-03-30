import string
import sys

NOTATION = string.digits+string.ascii_uppercase
num1 ,num2 = sys.stdin.readline().split()

def numeral_system(num1,num2):
    a,b=divmod(int(num1),int(num2))
    if a != 0 :
        return numeral_system(a,num2) + NOTATION[b]
    elif a == 0 :
        return NOTATION[b]
    
    
answer = numeral_system(num1,num2)
print(answer)

