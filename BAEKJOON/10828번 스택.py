# push X: 정수 X를 스택에 넣는 연산이다.
list.append(x)
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
if len(list)>0:
    print(list.pop()) 
else:
    print(-1)
# size: 스택에 들어있는 정수의 개수를 출력한다.
len(list)
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
if len(list)==0:
    print(True)
else:
    print(False)
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
if len(list)>0:
  print(list[len(list)-1])
else:       
   print(-1)
# ---------------------------------------------------

import sys

n=int(sys.stdin.readline())
list= [ ]

for _ in range(n):
    test=sys.stdin.readline().split()
    
    if test[0]== 'push':
        list.append(test[1])
    
    elif test[0]=='pop':
        if len(list)>0:
            print(list.pop())
        else:       
            print(-1)
        
    elif test[0]=='size':
        print(len(list))
        
    elif test[0]=='empty':
        if len(list)==0:
            print(1)
        else:
            print(0)

    elif test[0]=='top':
        if len(list)>0:
            print(list[len(list)-1])
        else:       
            print(-1)