import re
result = [] #result 리스트에 FBI 요원 번호 넣기
no = 0

for _ in range(5):
    t = input()
    p=re.compile('(FBI)')
    m=p.search(t)
    no+=1 #반복문 시행할 때마다 번호 하나씩커짐
    
    if m!=None: #FBI는 서치되니까 None이 아니다.
        result.append(no)        

if len(result)==0: 
    print('HE GOT AWAY!') 
else:
    for i in result:
        print(i,end=' ')