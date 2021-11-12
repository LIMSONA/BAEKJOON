# 나무높이v, 낮에a미터 올라가고 밤에 b미터 내려감
# 끝까지 올라가려면 며칠 걸리는지?
# 정상 도달 후 미끄러지지 않음

# 1차시도(시간초과)---------------------
import sys
a,b,v=map(int,input().split())

for i in range(1,sys.maxsize):
    
    if i*(a-b)<v<=i*(a-b)+a:
        print(i+1)
        break

#2차시도(성공)------------------------
a,b,v=map(int,input().split())

x=(v-b)/(a-b)
# x가 정수일수도 있고 소수일수도 있음
# 정수인경우: 낮시간 꼬박해서 정상 도달
# 소수인 경우: 낮시간 중간에 정상도달

#정수인 경우
if x==int(x):   
    print(int(x))

#소수인 경우 int하면 버림되니까 1 더해줌
else:   
    print(int(x)+1)