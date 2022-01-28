from sys import stdin
t=int(stdin.readline())

nums=[]
for i in range(t):
    nums.append(list(map(int,stdin.readline().split())))
nums.sort(key=lambda x:(x[0],x[1]))

for i in nums: print(i[0],i[1])