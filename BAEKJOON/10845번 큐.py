from collections import deque
from sys import stdin

n=int(stdin.readline())
pot=[]
pot=deque(pot)
    
for _ in range(n):
    text=stdin.readline().split()
    
    if text[0]=='push':
        pot.append(text[1])
    
    elif text[0]=='pop':
        if len(pot)!=0: 
            print(pot[0])
            pot.popleft()
        else: print(-1)
        
    elif text[0]=='size': print(len(pot))
    
    elif text[0]=='empty':
        if len(pot)==0: print(1)
        else: print(0)
        
    elif text[0]=='front':
        if len(pot)!=0: print(pot[0])
        else: print(-1)
        
    elif text[0]=='back':
        if len(pot)!=0: print(pot[-1])
        else: print(-1)