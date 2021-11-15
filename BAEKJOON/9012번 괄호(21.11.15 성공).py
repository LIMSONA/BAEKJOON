t=int(input())

for _ in range(t):
    data=list(input())
    result=[]

    for i in data:
        if i=='(':
            result.append(i)
        else: #i==')'
            if len(result)==0:
                result.append('아니지롱')
                break
            else:
                result.pop()
                
    if len(result)==0:
        print('YES')
    else:
        print('NO')
