# 1차시도 cnt를 이용해서 알아내기(실패)------------------

n=int(input())  #컴퓨터의 수
link=int(input())   #연결 쌍의 수

graph=[[0]*(n+1) for _ in range(n+1)]   #맵 프레임
visit=[0]*(n+1)     #방문기록 리스트


#맵 프레임에 자료 입력
for _ in range(link): 
    link1,link2=map(int,input().split())
    graph[link1][link2] = graph[link2][link1]=1     


def dfs(x):
    visit[x]=1
    for i in range(1,n+1):
        #조건: 방문기록 없고, 연결되어있으면
        if visit[i]==0 and graph[x][i]==1:  
            dfs(i)
            
dfs(1)
cnt=0
for i in range(1,n):
    if visit[i]==1:
        cnt+=1
print(cnt)


#4차시도 len을 이용하여 알아보기-----------------------------

n=int(input())  #컴퓨터의 수
link=int(input())   #연결 쌍의 수

graph=[[0]*(n+1) for _ in range(n+1)]   #맵 프레임
visit=[0]*(n+1)     #방문기록 리스트


#맵 프레임에 자료 입력
for _ in range(link): 
    link1,link2=map(int,input().split())
    graph[link1][link2] = graph[link2][link1]=1

result=[]
def dfs(x):
    visit[x]=1
    for i in range(1,n+1):
        #조건: 방문기록 없고, 연결되어있으면
        if visit[i]==0 and graph[x][i]==1: 
            result.append(i)
            dfs(i)
    return len(result)

print(dfs(1))