# 최대 공약수 
# 방법 1 (유클리드호제법)
def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)
    
# 방법 2 (math 내장함수)
a,b=map(int,input().split())

import math
print(math.gcd(a,b))

# --------------------------------------------------

#최소 공배수
#방법 1 (유클리드호제법 활용)
def lcm(a,b):
    if a%b==0:
        return a*b //gcd(a,b)
    else:
        return lcm(b, a%b)
    
#방법 2 (math 내장함수)
a,b=map(int,input().split())

import math
print(math.lcm(a,b))