t=input()
import re
p=re.compile('(pi|ka|chu)+')
if p.fullmatch(t): print('YES')
else: print('NO')