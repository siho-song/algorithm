A,B = list(map(int,input().split()))

def gcd(a,b):
    while b != 0 :
        a = a%b
        a,b = b,a
    return a

def lcm(a,b):

    return a*b//gcd(a,b)

print(gcd(A,B))
print(lcm(A,B))


#최대공약수 GCD(Greatest Common Divisor)
#최소공배수 LCM(Least Common Multiple)
# 유클리드 호제법 
# 유클리드 호제법은 2개의 자연수 또는 정수의 최대공약수를 구하는 알고리즘의 하나로, 호제법이란 말은 두 수가 서로 상대방 수를 나누어서 결국 원하는 수를 얻는 알고리즘을 나타낸다. 
# 2개의 자연수(또는 정수) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수(gcd)는 b와 r의 최대공약수와 같다. 
# 이 성질에 따라, b를 r로 나눈 나머지 r’를 구하고, 다시 r을 r’로 나눈 나머지를 구하는 과정을 반복하여 나머지가 0이 되었을 때 나누는 수가 a와 b의 최대공약수이다.