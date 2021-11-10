n,m = map(int,input().split())
array= list(map(int,input().split()))

start = 0
end = max(array)

#최적값 후보변수:result
result=0

while start<=end:
    mid=(start+end)//2
        
    #자른 떡들계산 변수: cut
    cut=0
        
    # 떡 잘랐을때 양 계산
    # 떡 자르기조건: 떡이 중간점보다 커야함
    for i in array:
        if i > mid:
            cut += i-mid
        
    #잘라나온 떡이 조금
    if cut< m:
        end = mid - 1
        
    #잘라나온 떡이 많음
    else:
        result = mid #최적값후보로 등록
        start = mid + 1

print(result)