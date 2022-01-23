a=list(map(int,input().split()))

if sum(a)>=100: print('OK')
else:
    if a.index(min(a))==0: print("Soongsil")
    elif a.index(min(a))==1: print("Korea")
    elif a.index(min(a))==2: print("Hanyang")

