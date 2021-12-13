# 실패==================================

import re
a=input()

p=re.sub(r'[^UCP]',"",a)

q= re.match('UCPC',p)
if q: print("I love UCPC")
else: print('I hate UCPC')

# 성공====================================

import re
a=input()

p=re.sub(r'[^UCP]',"",a)
q= re.match('.*U+.*C+.*P+.*C+.*',p)

if q: print('I love UCPC')
else: print('I hate UCPC')