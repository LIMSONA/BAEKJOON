#  유클리드 호제법 : 두 자연수 A,B(A>B)에서 A%B==R이면, 
#  A와B의 최대공약수는 B와R의 최대공약수와 동일 

def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(b, a%b)

print(gcd(18,17))