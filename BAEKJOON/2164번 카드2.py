from collections import deque

n=int(input())
d= deque(list(range(1,n+1)))

while len(d)>1 :
    d.popleft()
    switch= d.popleft()
    d.append(switch)
    
print(d[0])
    