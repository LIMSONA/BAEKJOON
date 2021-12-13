#실패=========================

import re

while True:
    a=input()
    p=re.match('problem', a.lower())
    if p: print('yes')
    else: print('no')
    
    
#성공===================================== 
import re
while True:
    try:
        a=input()
        p=re.match('.*problem+', a.lower())
        if p: print('yes')
        else: print('no')
    except EOFError: break