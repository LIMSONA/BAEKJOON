a,b=map(int,input().split())
x= a//b
y= a%b
if y<0 and a!=0:
    x+=1
    y-=b
    
print(x)
print(y)