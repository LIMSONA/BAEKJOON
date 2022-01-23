# 소들의 수 N, 헛간의 크기 W  H 소들에게 배정되는 공간의 크기 L
n,w,h,l=map(int,input().split())

if w<l or h <l: print(0)
else:
    if (w//l) * (h//l) >=n: print(n)
    else: print((w//l) * (h//l))