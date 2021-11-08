n = int(input())    #지도 가로,세로


graph = []  #맵 데이터 넣기
for _ in range(n):
    graph.append(list(map(int,input())))

result = [] #아파트 로드맵
cnt = 0  #아파트안 집 갯수 세기

dx = [0,0,1,-1] #동서남북 인접한 곳의 좌표를 구하기 위함 
dy = [1,-1,0,0]


def dfs(x,y):
    global cnt
    graph[x][y] = 0   #방문한 곳을 따로 체크하는 visit 리스트를 만들기보다 0으로 만들어서 체크를 하는 게 이득
    cnt += 1 #탐색을 시작할 때마다 카운트를 더해준다 
    for k in range(4): #동서남북 인접한 네 방향에 대해서 
        nx = x + dx[k]
        ny = y + dy[k]
        if nx<=-1 or ny<=-1 or nx>=n or ny>=n: #맵 안에서 찾을 수 있게 제한
            continue    
        if graph[nx][ny] ==1: #인접한 곳의 좌표가 범위 내이고, 1이라면 
            dfs(nx,ny) #조건을 만족하는 지점에서 다시 탐색을 시작한다 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i,j)
            result.append(cnt)


print(len(result)) # 아파트 동 갯수 구하기
# result= [7,8,9] 우연히 오름차순으로 리스트에 들어감

result.sort()   #오름차수 정렬
for i in result:    #각 리스트의 cnt 꺼내고
    print(i)