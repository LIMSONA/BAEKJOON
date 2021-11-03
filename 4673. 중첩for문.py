
# (1~10000)에서 - (생성자 있는 숫자를 빼야함)


# n은   d(n)의    생성자
# 33은  39의      생성자
# (x)   셀프넘버



base=set(range(1,10001))
n = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    n.add(i)
result = base - n
for real in sorted(n):
    print(real)
