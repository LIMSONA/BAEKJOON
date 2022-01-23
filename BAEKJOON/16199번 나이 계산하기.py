a=list(map(int,input().split()))
b=list(map(int,input().split()))

#만 나이 
if b[1]==a[1]:
    if b[2]>=a[2]: print(b[0]-a[0])
    else: print(b[0]-a[0]-1)

elif b[1]>a[1]: print(b[0]-a[0])
       
elif b[1]<a[1]: print(b[0]-a[0]-1)
    
#세는 나이
print(b[0]-a[0]+1)
#연 나이
print(b[0]-a[0])