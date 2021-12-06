# 실패:4에서 빼면 안됨------------------
# 반례:AaaaBbbbCccccccD 
import re

text= input()
sp_list=re.split('(?=[A-Z])',text)
cnt=0
for i in range(1,len(sp_list)-1):
    a= 4-len(sp_list[i])
    if a>0: cnt+=a  
print(cnt)

# ----------------------------------------

import re
t = input()
p = re.split('(?=[A-Z])',t)
cnt = 0    
for i in range(1,len(p)-1):
    a= len(p[i]) % 4
    if a!= 0: cnt+= (4-a)    
print(cnt)