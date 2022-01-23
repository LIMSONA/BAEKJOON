n=int(input())

if n ==0: print("divide by zero")
else:
    rec=list(map(int,input().split()))

    #평균 a
    a = sum(rec)/n

    #기댓값 b
    set_rec=set(rec)
    b=0
    for i in set_rec:
        b += i*(rec.count(i)/n)

    result = a/b
    print('%.2f'%result)
