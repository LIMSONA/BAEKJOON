n,m,k=map(int,input().split())

#앞면 m개 o표시/n-m개 x표시
om=m
xm=n-m
#뒷면 k개 o표시/n-k개 x표시
ok=k
xk=n-k

print( min(om,ok) + min(xm,xk) )