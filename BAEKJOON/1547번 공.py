# 첫째 줄에 컵의 위치를 바꾼 횟수 M, M은 50보다 작거나 같은 자연수
# 둘째 줄부터 M개의 줄에는 컵의 위치를 바꾼 방법 X와 Y가 주어지며, 
# X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미한다. 
# X와 Y의 값은 3보다 작거나 같고, X와 Y가 같을 수도 있다.

m = int(input())

ball= 1
for _ in range(m):
    mix = list(map(int,input().split()))
    if ball in mix:
        mix.remove(ball)
        ball = mix[0]
    else: pass
    
print(ball)
        
    