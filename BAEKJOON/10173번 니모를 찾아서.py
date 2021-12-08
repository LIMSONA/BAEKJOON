import re
while True:
    sen=input()
    if sen=='EOI': break #스톱 식 끝내기
    
    #소문자로 바꾼 문장 중 니모찾기
    p=re.findall('.nemo.',sen.lower()) 
    if len(p)!=0: print("Found")
    else: print("Missing")