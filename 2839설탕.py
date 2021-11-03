n=int(input())
pouch=0

while n>=-0:
    if n%5==0:
        pouch+=(n//5)
        print(pouch)
        break
    n-=3
    pouch+=1
else:
    print(-1)




