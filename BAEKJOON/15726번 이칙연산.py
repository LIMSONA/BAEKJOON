# 한 번의 곱셈 기호와 한 번의 나눗셈
a,b,c=map(int,input().split())

result=max(a*b/c, a/b*c)
print(int(result))