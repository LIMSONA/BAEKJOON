import sys

n,m=map(int,sys.stdin.readline().split())
woods=list(map(int,sys.stdin.readline().split())) #나무 값들

start=0
end=max(woods)

result=0   #정답 후보

while start<=end :
    
    mid=(start+end)//2   #중간값
    get=0 #자르고 남은 나무

    
    get=sum(i-mid if i>mid else 0 for i in woods)
    # for i in woods:
    #     if i>mid:
    #         get += i-mid
        
    if get < m:
        end= mid-1  
    else: # get >= m:
        result = mid
        start = mid+1

print(result)