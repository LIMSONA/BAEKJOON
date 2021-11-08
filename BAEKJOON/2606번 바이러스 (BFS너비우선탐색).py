# 1~3차시도(실패)-----------------------------------
n=int(input())  #컴퓨터 수
link=int(input())   #연결 수

graph=[[0]*(n+1) for _ in range(n+1)] #맵프레임
visit=[0]*(n+1) #방문기록 체크

for _ in range(link):   #맵 데이터 만들기
    link1,link2=map(int,input().split())
    graph[link1][link2]=graph[link2][link1]=1

from collections import deque

def bfs(x):
    que=deque()     #큐형식
    que.append(x)   #방문 검사할 리스트
    visit[x]=1      #방문했으니 1로 체크
    
    while que:
        x=que.popleft()
        for i in range(n+1):
            if visit[i]==0 and graph[x][i]==1:
                que.append(i)   #검사할 숫자리스트 넣기
                visit[i]=1  #검사했으니 1로 체크
    return que

print(len(bfs(1)) - 1)  #원인이 되었던 1번 컴퓨터 1대는 빼야함


# 4차 시도------------------------------------

n=int(input())  #컴퓨터 수
link=int(input())   #연결 수

graph=[[0]*(n+1) for _ in range(n+1)] #맵프레임
visit=[0]*(n+1) #방문기록 체크

for _ in range(link):   #맵 데이터 만들기
    link1,link2=map(int,input().split())
    graph[link1][link2]=graph[link2][link1]=1

from collections import deque

def bfs(x):
    result=[x]      #걸린 컴퓨터 알아보기
    que=deque()     #큐형식
    que.append(x)   #방문 검사할 리스트
    visit[x]=1      #방문했으니 1로 체크
    
    while que:
        x=que.popleft()
        for i in range(n+1):
            if visit[i]==0 and graph[x][i]==1:
                result.append(i)    #걸린 컴퓨터리스트 넣기
                que.append(i)   #검사할 숫자리스트 넣기
                visit[i]=1  #검사했으니 1로 체크
    return result

# result=[1,2,5,3,6]
print(len(bfs(1)) - 1)  #원인이 되었던 1번 컴퓨터 1대는 빼야함