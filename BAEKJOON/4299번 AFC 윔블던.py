import sys

# 합과 차를 공백구분으로 하는 정수를 입력받음
sum, sub = map(int, sys.stdin.readline().split())

# 이루어질 수 없는 경우들  ==> -1 출력
    # step1 - 점수 차(sub)가 점수 합(sum)보다 큰 경우
    # step2 - (sum+sub)와 (sum-sub)가 2의 배수가 아닌 경우 (=홀수인 경우)
if sub>sum or (sum+sub)%2==1 or (sum-sub)%2==1 : 
    print(-1)
    
# 이외는 정상적인 경우이므로, 큰 점수 x 
else: 
    print( (sum+sub)//2, (sum-sub)//2  )
    
    