# m줄의 수가 N줄에 들어있는가?
# m이 들어있으면 1 true 없으면 2 false

n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)