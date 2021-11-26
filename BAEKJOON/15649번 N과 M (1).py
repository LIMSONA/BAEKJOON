import itertools

m,n=map(int,input().split())

result=itertools.combinations(range(1,m+1),n)

for i in result:
    
    
    