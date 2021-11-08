#n*n 맵크기
#첫째줄 총 단지 수
#둘째줄~ 각 단지마다 집의 개수

n=int(input()) #지도의 크기
graph=[]
#맵 데이터 받기
for _ in range(n):
    graph.append(list(map(int,input())))


result = [] #아파트 로드맵
cnt = 0  #아파트안 집 갯수 세기


def dfs(x,y):
    global cnt
    if x<=-1 or y<=-1 or x>=n or y>=n:
        return
    if graph[x][y]==1:
        graph[x][y]=0
        cnt+=1
        dfs(x-1,y)  #왼쪽
        dfs(x+1,y)  #오른쪽  
        dfs(x,y-1)  #아래
        dfs(x,y+1)  #위
        return


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)


print(len(result))
result.sort()
for i in result:
    print(i)