# 첫째줄 세로,가로 입력받기
n, m = map(int,input().split())

# 둘째줄~ 입력값 리스트로 만들어 맵 만들기
graph=[ ]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m: #맵 안에서 찾을 수 있게 제한
        return False
    if graph[x][y]==0:  #조건: 방문하지 않아서 False 0이라면
        graph[x][y]=1   #조건: 방문한 증표로 True 1로 기록
        dfs(x-1,y)  #왼쪽
        dfs(x+1,y)  #오른쪽  
        dfs(x,y-1)  #아래
        dfs(x,y+1)  #위
        return True

result=0  #방문한 곳 체크 하기 위해 result 만들기
for i in range(n):  #세로길이 반복
    for j in range(m):  #가로길이 반복
        if dfs(i,j) ==True: #조건: 방문해서 True 1이라고 한다면
            result+=1   #방문된 곳을 체크하기위해 카운트
print(result)