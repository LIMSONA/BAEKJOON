# 첫째 줄에 1m2당 사람의 수 L (1 ≤ L ≤ 10)과 파티가 열렸던 곳의 넓이 P (1 ≤ P ≤ 1000)가 주어진다.

# 둘째 줄에는 각 기사에 실려있는 참가자의 수가 주어진다. 106보다 작은 양의 정수 5개가 주어진다.

상근=list(map(int,input().split(" ")))
news=list(map(int,input().split(" ")))

people= 상근[0]*상근[1]
for i in news:
    print(i-people,end=" ")
