n=int(input())
base=[n//10,n%10]
result=base[:]
cnt=0
while 1:
    next=[base[1],(sum(base)%10)]
    base=next
    cnt+=1
    if next==result:
        print(cnt)
        break



n=int(input())
num=n
cnt=0

while 1:
    a=num//10
    b=num%10
    c=(a+b)%10
    num=(b*10)+c

    cnt+=1
    if (num==n):
        break