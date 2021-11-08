# 정점번호 작은것부터 방문 
# 정점개수n, 사이 선개수m, 시작정점번호v
# 첫째줄 DFS 결과 방문순서
# 둘째줄 BFS 결과 방문순서

n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]   #맵 프레임 만들기
visit=[0] *(n+1)    #방문한 정점 체크 리스트

#맵 프레임에 자료 입력
for _ in range(m): 
    m1,m2=map(int,input().split())
    graph[m1][m2] = graph[m2][m1]=1
  
#dfs 깊이우선 탐색
def dfs(x):     #x부터 시작
    visit[x]=1      #방문한 정점은 1로 체크
    print(x,end=" ")     #방문한 정점 출력  
    for i in range(1,n+1):  
        # 조건: (방문하지 않아서 visit 리스트에 0으로 체크) 
        # and (맵에서 연결되어있다고 1이라고 표시되있는 경우)
        if visit[i]==0 and graph[x][i]==1:  
            dfs(i)  #계속 이어서 진행


#bfs 넓이우선 탐색
from collections import deque

def bfs(x):     #x부터 시작
    que=deque()
    que.append(x)     #연결된 정점넣을 리스트
    visit[x]=1      #방문한 정점은 1로 체크

    while que:
        x=que.popleft()     #왼쪽부터 꺼내기
        print(x,end=" ")     #방문한 정점 출력
        for i in range(1,n+1):
            #조건: (방문하지 않아서 리스트에 0으로 체크)
            #and (맵에서 연결되어있다고 1이라고 표시되있는 경우)
            if visit[i]==0 and graph[x][i]==1:
                que.append(i)   #조건만족하면 연결정점리스트에 넣기
                visit[i]=1      #그 다음 방문할 i정점에 방문했다고 1 표시


dfs(v)
print()     #줄바꿈하고

visit=[0]*(n+1) #다시 깨끗하게 리스트 만들고
bfs(v)