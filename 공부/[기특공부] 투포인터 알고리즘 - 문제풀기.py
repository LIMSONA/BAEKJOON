n=int(input()) #데이터 개수
m=int(input()) #찾고자하는 부분 합
data=list(map(int,input().split())) #전체 수열리스트

cnt = 0    #찾은 개수 카운트
interval_sum = 0    #간격
end = 0    #끝점

for start in range(n):  #시작점 증가
    
    #간격 합이 작거나 끝점이 data 마지막 위치 되기 전
    while interval_sum < m and end< n:
        interval_sum += data[end]
        end += 1 #끝점 하나씩 옆으로 이동하여 간격 넓히기
        
        if interval_sum == m:
            cnt+=1 # 찾음
            
        #시작점 옆으로 움직이기 전 시작값 더한 건 빼기    
        interval_sum -= data[start] 
        
print(cnt)













