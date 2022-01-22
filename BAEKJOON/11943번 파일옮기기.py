a=list(map(int,input().split())) #a바구니
b=list(map(int,input().split())) #b바구니

print(min(a[0]+b[1],a[1]+b[0]))


# #양쪽바구니 사과=배 
# if len(set(a))==1 and len(set(b))==1: print(a[0]+b[0])
# #한쪽바구니 사과=배
# elif len(set(a))==1: print(min(b)+a[0])
# elif len(set(b))==1: print(min(a)+b[0])
# #양쪽 바구니 사과!=배
# else: 

# if sum(a)<=sum(b): #b바구니 총합이 많으면
#     if b[0]<=b[1]: print(b[0]+a[1])
#     elif b[0]==b[1]:
#         if 
#     else: print(b[1]+a[0])    

# elif sum(a)<sum(b): #a바구니 총합이 많으면
#     if a[0]<=a[1]: print(a[0]+b[1])
#     else: print(a[1]+b[0])
 
    
