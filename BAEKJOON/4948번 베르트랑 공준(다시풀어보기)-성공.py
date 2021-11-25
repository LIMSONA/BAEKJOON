#문제 포인트!!!!!
#n의 값이 1 ≤ n ≤ 123,456 제한 되어있으니
#미리 123456값까지 소수를 구해놓는것!!!


max = 123456 # n의 범위의 최댓값

#소수 판별을 위한 리스트array 설정(소수는 True, 아니면 False)
array = [True for _ in range(2*max+1)] 

#0과 1은 미리 False 설정
array[0], array[1] = False, False 

# 에라토스테네스의 체 공식
import math
#2부터 int(math.sqrt(2*123456) 인덱스까지 확인
for i in range(2, int(math.sqrt(2*max)+1)): 
    
    if array[i]==True:
        j=2 
        while i*j <= 2*max: #i*j 가 2*123456 보다 작거나 같다면
            array[i*j]=False #해당 i*j의 값은 소수가 아니므로 False로 설정
            j+=1 #j를 1씩 증가

# 기본정보 입력 및 답 출력
while True:
    n = int(input())
    if n == 0: #0이면 반복문 탈출
        break
    
    #array 슬라이싱하고 count!
    print( array[n+1 : 2*n+1].count(True) )