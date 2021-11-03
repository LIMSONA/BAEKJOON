# n개의 수. 오름차순 정렬
# 첫째줄 개수. 둘째중부터 숫자

n=int(input())
nums=list()
for _ in range(n):
    num=int(input())
    nums.append(num)
    nums.sort()

for i in nums:
    print(i)

