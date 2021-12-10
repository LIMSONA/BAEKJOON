#0부터 시작하니 6번자리를 알고싶다면 7번째자리를 찾아야한다.

n,m,num=map(int,input().split())

x= (num)//m
y= (num)%m

print(x,end=" ")
print(y)