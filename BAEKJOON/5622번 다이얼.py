alpha=['뿅','뿅','뿅','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=input()

cnt=0

for i in word:
    for j in range(0,len(alpha)):
        if i in alpha[j]:
            cnt+=j #인덱스 값 더하기
            break
            
print(cnt)