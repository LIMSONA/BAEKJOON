a = input()
cyc = (len(a)//10) +1
i = 0

for _ in range(cyc):
    print(a[0+i:10+i])
    i+=10
