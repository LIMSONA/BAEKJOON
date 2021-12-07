# True는 1
# False는 0

############# and와 &와 +와 , 차이
print(2 & 3) #>>> 2
print(2 and 3) #>>> 3
print(2 + 3) #>>> 5
print(2 , 3) #>>> 2 3

############# or와 | 차이
print(2 | 3) #>>> 3
print(2 or 3) #>>> 2


############# ==와 is 차이
a = []
b = []
c = a

print(id(a))
print(id(b)) #a와 id값 다름
print(id(c)) #a와 id값 같음

print(a == b) #>>> True
print(a == c) #>>> True
print(b == c) #>>> True

print(a is b) #>>> False
print(a is c) #>>> True
print(b is c) #>>> False