
# (1~10000)에서 - (생성자 있는 숫자를 빼야함)


# n은   d(n)의    생성자
# 33은  39의      생성자
# (x)   셀프넘버

base=set(range(1,1001))

n=1
result = set()
while 1:
   a = set()
   a.add(n)
   b=n+sum(a)
   n+=1
   result.add(b)
   if b==10:
    for i in (base-result):
        print(i)
        break 