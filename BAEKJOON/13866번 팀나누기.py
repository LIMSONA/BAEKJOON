a=list(map(int,input().split()))

g1=min(a)+max(a)
g2=sum(a) - (min(a)+max(a))

print(abs(g1-g2))