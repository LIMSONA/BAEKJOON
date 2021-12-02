import re

a=input()
b=input()

p=re.compile(b)
m=p.findall(a)
print(len(m))

