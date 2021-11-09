# 시간제한 0.25초
# 첫째줄 테스트 개수 t
# 둘째줄 0 출력 횟수, 1 출력 횟수

# 1차시도(실패)-------------------------------

import sys
t= int(sys.stdin.readline())

fibo=[[0],[1]]
for i in range(2,41):
    fibo.append(fibo[i-1]+fibo[i-2])
    
for _ in range(t):
    num=int(sys.stdin.readline())
    # fibo[num] 속에 0과 1카운트
    sys.stdout.write(fibo[num].count(0))
    sys.stdout.write(fibo[num].count(1))

# 2차시도(성공)------------------------

import sys
t=int(sys.stdin.readline())

for _ in range(t):
    n=int(sys.stdin.readline())
    # 0 기준으로
    zero = 1
    one = 0
    for _ in range(n):
        #다음 수 zero는 현재one값
        #다음 수 one은 현재zero+one값
        one_clone = one
        one= zero + one
        # zero = one를 바로 쓰면 안됨. 
        # one은 바뀌어있는 상태임 그러니 미리 clone을 만들어야함(33번줄에 추가)
        zero= one_clone
    print(zero, one)
        