n,m=map(int,input().split())
woods=list(map(int,input().split())) #나무 값들

start=min(woods)
end=max(woods)

result=[]   #정답 후보리스트

while start<=end :
    
    mid=(start+end)//2   #중간값
    get=0 #자르고 남은 나무

    for i in woods:
        if i>mid:
            get += i-mid
        
    if get < m:
        end= mid-1
        
    elif get == m:
        result.append(mid)
        break
    
    elif get > m:
        result.append(mid)
        start = mid+1

print(max(result))
