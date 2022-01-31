n,k= map(int,input().split())
a= list(range(1,n+1))
result=[]

index = 0
while a:
    index += k-1
    if index >=len(a):
        index %= len(a)
    result.append(str(a.pop(index)))
    
print('<'+ ', '.join(map(str, result)) + '>')