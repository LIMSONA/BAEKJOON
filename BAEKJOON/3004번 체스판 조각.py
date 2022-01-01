n = int(input())
result = 1
a = 1

for i in range(n):
    result += a
    if i%2 == 0:
        a += 1
        
print(result) 