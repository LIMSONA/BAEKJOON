import re

t= int(input())

for _ in range(t):
    test=input()
    
    p=re.compile('(100+1+|01)+')
    
    #match가 아닌 fullmatch를 쓰는게 이 문제의 핵심!
    if p.fullmatch(test): print('YES')
    else: print('NO')    
