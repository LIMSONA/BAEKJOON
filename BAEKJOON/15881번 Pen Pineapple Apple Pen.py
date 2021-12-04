# 사과는 A로, 파인애플은 P로 대문자, 펜은 p로 소문자
# pPAp

n=input()
m=input()

import re
p=re.compile('(pPAp)')
m=p.findall(m)
print(len(m))