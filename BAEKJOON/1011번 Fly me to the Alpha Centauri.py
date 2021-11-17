t=int(input())

for _ in range(t):
    x,y=map(int,input().split())
    거리=y-x
    n=1
    while True:
        if 거리>n*(n+1):
            n+=1
        else: #거리<=n*(n+1)
            #거리는 n그룹에 있음
            if 거리<=(n**2): #->n그룹의 상단
                print(n*2-1)
                break
            else: #거리>(n**2) ->n그룹의 하단 
                print(n*2)
                break