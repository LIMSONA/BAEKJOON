#[1] 딕셔너리 만들기====================
# chr(97)은 a이니까
dic =dict()
i= 97
num= 1
while i!=123:
    dic[chr(i)]=num
    i+=1
    num+=1

#[2] 값 계산하여 결과 도출하기===========
t= int(input())
test= str(input())
result=0
cnt=0
for i in range(t):
    result+= (dic[test[i]]*31**cnt) %1234567891
    cnt+=1
print(result%1234567891)