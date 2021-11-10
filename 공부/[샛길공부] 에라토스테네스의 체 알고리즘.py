import math

n= int(input()) 

#처음엔 모두 소수(True)라고 리스트 만들기
#소수가 아니라면 False로 제거처리
array=[True for _ in range(n+1)]

# 2부터 제곱근까지 모든 수 확인하기
for i in range(2,int(math.sqrt(n)+1)):
    
    #조건: 리스트안 남은 수가 소수인 경우
    if array[i] == True:
        
        j=2 #자신은 포함시키면 안되니까 2부터 시작 
        while i*j <=n: #i의 배수를 제거처리
            array[i*j] = False
            j+=1
                        
#array 반복 돌면서 살아남은 소수(True) 조회
for k in range(2, n+1):
    if array[k]: 
        print(k, end=" ")
