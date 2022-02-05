# 간단하게 써보기 ===========================
t= int(input())
test= str(input())
result=0
for i in range(t):
    result+= (ord(test[i])%96)*31**i %1234567891
print(result %1234567891)
