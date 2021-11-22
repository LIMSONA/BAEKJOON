a,b = map(int,input().split())


#최대공약수(유클리드호제법)
def result_1(a,b):
    if a%b==0:
        return b
    else:
        return result_1(b, a%b)

c,d=a,b
#최대공배수(최대공약수로 나눈 몫들과 최대공약수를 곱한 값)    
def result_2(a,b):
    if a%b==0:
        return int(b*(c/b)*(d/b))
    else:
        return result_2(b, a%b)
    
print(result_1(a,b))
print(result_2(a,b))