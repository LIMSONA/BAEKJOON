x,y,w,h=map(int,input().split())

# (x.y)점 기준으로 직사각형에 직선으로 그었을 때 최단거리를 구하면 됨
print(min(x, y, w-x, h-y))

# 엄청 긴 답지
if x==w/2 and y==h/2:
    if x>y:
        print(y)
    else: 
        print(x)

else:
    if x>w/2:
        a=w-x
    else: #x<w/2
        a=x

    if y>h/2:
        b=h-y
    else: #y<h/2
        b=y

    if a>b:
        print(b)
    else:
        print(a)
    