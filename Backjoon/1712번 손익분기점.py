# import sys
# a,b,c= map(int,input().split(" "))
# for i in range(1, sys.maxsize):
#     if (c-b)*i<=a:
#         pass
#     elif (c-b)*i>a:
#         print(i)
#         break
#     else:
#         print(-1)

a,b,c= map(int,input().split(" "))

if c-b<=0:
    #노트북가격 - 생산가격 <= 0
    print(-1)
else:
    #(노트북 가격 - 생산가격) * X > 고정비용
    #X = 고정비용 / (노트북가격 - 생산가격) =>>>> 순이익: X + 1
    #1000 / 100 = 10 + 1
    print(int(a/(c-b) + 1))






