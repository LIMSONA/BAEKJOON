# 마지막 네번째 점의 경우
# 앞에 나왔던 점중 하나만 나온 점을 출력하면 된다.

data=[[] for _ in range(2)]

for _ in range(3):
    m,n= map(int,input().split())
    data[0].append(m)
    data[1].append(n)
    
i=0
while i<2:
    if data[i][0]==data[i][1]:
        print(data[i][2],end=' ')
        
    elif data[i][0]==data[i][2]:
        print(data[i][1],end=' ')
    else:
        print(data[i][0],end=' ')
    i+=1


# -----다른 방법-----------

data=[[] for _ in range(2)]

for _ in range(3):
    m,n= map(int,input().split())
    data[0].append(m)
    data[1].append(n)
    
for i in range(3):
    if data[0].count(data[0][i]) == 1:
        x = data[0][i]
    if data[1].count(data[1][i]) == 1:
        y = data[1][i]
print(x, y)