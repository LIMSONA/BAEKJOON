import sys

num=[]
for _ in range(5):
    score=int(sys.stdin.readline())
    if score<40:
        score=40
    num.append(score)

print(int(sum(num)/5))        