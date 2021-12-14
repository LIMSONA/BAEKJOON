#실패=========================

import re
while True:
    a=input()
    p=re.match('problem', a.lower())
    if p: print('yes')
    else: print('no')
    
    
#성공===================================== 
import re
while True: #입력이 반복될 거니까
    try:
        a=input()
        #대소문자 구분하지 않도록 lower()하거나 또는
        #re.match('.*problem', a, re.I)로 대소문자 무시한다.
        p=re.match('.*problem', a.lower())
        if p: print('yes')
        else: print('no')
    except EOFError: break #입력이 끝나면 break