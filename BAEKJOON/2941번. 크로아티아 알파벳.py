# 알파벳 변경하여 입력
# 주어진 단어가 몇 개의 알파벳으로 이루어져 있는지
# 8개의 크로아티아 알파벳을 a~z까지 있는 문자열 리스트에 추가하여 입력


# 1차 시도
# in을 써서 찾으면 공백으로 넣고 cnt에 1을 더하기 

cro=['c=','c-','dz=','d-','lj','nj','s=','z=']

n=input()

cnt=0
for i in cro:
    if i in n:
        n=n.replace(i," ")  # 찾아서 없애고 공백을 넣는다.(1칸을 띄워야함)
        cnt+=1
n=n.replace(" ","")  #나중에 갯수를 샐때 공백을 뺴줘야하니까
print(len(n)+cnt)




# 2차시도
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n = input()

for i in cro:
    if i in n:
        n = n.replace(i,'얍')  # 찾아서 '얍'이라고 바꾸고

print(len(n)) 
