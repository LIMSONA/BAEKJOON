#반복문--------------------
a=input().split('-') #하이픈으로 나누고
for i in a: print(i[0],end="") #가장 처음 대문자 출력
    
#정규표현식------------------------
import re
b=input()
test1=re.findall('[A-Z]+',b) #대문자만 찾고(리스트로찾음)
for i in test1: print(i,end="") #반복문으로 빼냄