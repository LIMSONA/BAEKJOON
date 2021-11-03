import string
u_alpha=list(string.ascii_uppercase)   #알파벳
n=str(input()).upper()      #대문자로 변환하여 리스트              
print(n)
y=list()                        #각 알파벳 카운트 값 리스트
for i in u_alpha:
    x=n.count(i)
    y.append(x)
print(y)
if y.count(max(y))>1:
    print("?")
else:
    # print(max(y))
    # print(y.index(max(y)))
    print(u_alpha[y.index(max(y))])