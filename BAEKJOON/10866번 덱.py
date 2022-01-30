import sys

def push_front(x) :
    li.insert(0, x)

def push_back(x) :
    li.append(x)

def pop_front() :
    if li : return li.pop(0)
    else : return -1

def pop_back() :
    if li : return li.pop()
    else : return -1

def size() : return len(li)

def empty() :
    if li : return 0
    else : return 1

def front() :
    if li : return li[0]
    else : return -1

def back() :
    if li : return li[-1]
    else : return -1

t = int(sys.stdin.readline())
li = []

for _ in range(t) :
    a = sys.stdin.readline().rstrip().split()
    if a[0] == 'push_front' :
        push_front(a[1])
    elif a[0] == 'push_back' :
        push_back(a[1])
    elif a[0] == 'pop_front' :
        print(pop_front())
    elif a[0] ==  'pop_back' :
        print(pop_back())
    elif a[0] == 'size' :
        print(size())
    elif a[0] == 'empty' :
        print(empty())
    elif a[0] == 'front' :
        print(front())
    elif a[0] == 'back' :
        print(back())


# t=int(input())
# li= list()

# for i in range(t):
#     a= input().split()
#     if a[0]=="push_front":
#         li.insert(0,a[1])
#     elif a[0]=="push_back":
#         li.append(a[1])
#     elif a[0]=="pop_front":
#         if len(li)==0: print(-1)
#         else: print(li.pop(0))
#     elif a[0]=="pop_back":
#         if len(li)==0: print(-1)
#         else: print(li.pop(-1))
#     elif a[0]=="size":
#         print(len(li))
#     elif a[0]=="empty":
#         if len(li)==0: print(1)
#         else: print(0)
#     elif a[0]=="front":
#         if len(li)==0: print(-1)
#         else: print(li[0])
#     elif a[0]=="back":
#         if len(li)==0: print(-1)
#         else: print(li[-1])

