t= int(input())
member=[] # member들 받기
for i in range(t):
    a=list(input().split())
    member.append(a)

member.sort(key= lambda x: int(x[0]))

for i in member: print(i[0],i[1])
