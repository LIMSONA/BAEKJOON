# 단순 반복문---------------

모음=['a','e','i','o','u']
while True:
    test= input()
    cnt= 0
    
    # '#'나오면 끝
    if test=='#' : break
    
    test= test.lower() #소문자로 바꾸기
    for i in test:
        if i in 모음: cnt+=1
    print(cnt)


# 정규표현식---------------

import re
while True:
    test= input()
    if test=='#' : break
    test= test.lower()
    
    p= re.findall('a|e|i|o|u',test)
    print(len(p))