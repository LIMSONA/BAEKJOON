# 첫째줄 세로,가로 입력받기
n, m = map(int, input().split())

# 둘째줄~ 입력값 리스트로 만들어 맵 만들기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0] #왼쪽/오른쪽/-/-
dy=[0,0,-1,1] #-/-/아래/위

#큐 표현을 위해 deque 라이브러리 사용!
from collections import deque  
def bfs(x,y):
    que= deque()
    que.append((x,y)) #x,y 같이 입력 
    
    while que: #큐가 빌때까지 반복하기
        x,y=que.popleft() #실행할 점을 하나씩 빼오기
        for i in range(4): #현재 지점에서 상하좌우 확인
            nx= x + dx[i] #왼쪽/오른쪽/-/-
            ny= y + dy[i] #-/-/아래/위
            if nx<0 or ny<0 or nx>=n or ny>=m: #맵 안에서 찾을 수 있게 제한
                continue    #for문으로
            if graph[nx][ny]==0: #괴물이 있는 곳
                continue    #for문으로
            if graph[nx][ny]==1: #괴물 없고, 처음 방문하는 곳
                graph[nx][ny] = graph[x][y] + 1 #이동거리를 표시하기위해 1 더하기
                que.append((nx,ny)) # 그 다음 이동을 위해 que에 집어 넣기
    return graph[n-1][m-1]  #가장 오른쪽 아래까지 도착했을때 더했던 값을 반환
    #n-1 m-1로 표기한 이유는, n과m은 자연수여서 1부터 시작 (1,2,3....)
    # 리스트 graph는 리스트여서 0부터 시작(0,1,2.....)


print(bfs(0,0))

