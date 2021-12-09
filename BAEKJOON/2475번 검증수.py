num=map(int,input().split(" "))
cnt=0
for i in num:
    a=i**2
    cnt+=a
print(cnt%10)