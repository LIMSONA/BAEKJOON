#1차시도: 반복문으로 하나씩 꺼내면서 제외시키고 반복문 돌리고 
n,m= map(int,input().split())
card=list(map(int,input().split()))
candi=[ ]   

for i in card:
    card.remove(i)
    for j in card:
	    card.remove(j)
	    for k in card:
        	candi.append(i+j+k)

result=[i for i in candi if i <=m]
print(max(result))		


#2차시도: 반복문으로 앞에서부터 하나씩 꺼내고 
#그 다음껀 앞에꺼 제외하고 또 반복돌리고~또제외하고 돌리고 나온 조합들 리스트에 넣기

n,m= map(int,input().split())
card=list(map(int,input().split()))
candi=[ ]     #candi 후보 리스트에 넣기

for i in range(n):
   for j in range(i+1,n):
       for k in range(j+1,n):
       	candi.append(card[i]+card[j]+card[k])

result=[i for i in candi if i <=m]
print(max(result))		