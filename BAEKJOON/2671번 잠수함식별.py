# (100~1~|01)~ 잠수함 소리 ~1개이상
# 잠수함의 엔진 소리에 해당하는 스트링이면 "SUBMARINE"을 출력하고, 그렇지 않으면 "NOISE"

import re
p=re.compile('(100+1+|01)+') #~는 1개이상이니 +으로 바꾸기

string= input()
if p.fullmatch(string): print('SUBMARINE') 

else: print('NOISE')