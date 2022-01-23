# 기차의 속도 S,  
# 파리의 속도 T, 
# 그리고 처음 두 기차 사이의 거리 D가 주어졌을 때 
# 두 기차가 만날 때까지 파리의 이동거리 F를 계산하는 프로그램을 작성


def fly(s,t,d):
    f= (d/(s*2))*t
    return int(f)

s,t,d= map(int,input().split())
print(fly(s,t,d))