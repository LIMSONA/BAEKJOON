n=int(input())
inp=map(int,input().split(" "))
result=0

for i in inp:
    cnt=0
    if i>1:
        for j in range(2,i):
            if i%j==0:
                cnt+=1
                break
        if cnt==0:
            result+=1
print(result)
        