#생성자 출력하는 걸 다 구하고
#범위 내에서 생성자 빼서 셀프넘버구하기

# 2부터 시작해서 돌려가면서 다 제거
# 그 다음 넣고 다 돌려서 제거 하고
#에라토스테네스의 체 응용

data=[True for _ in range(101)]
data[0]=None

for x in range(1,101):
    if data[x]==True:
        while x<101:
            y=(x//10)+(x%10)+x
            if y<101:
                data[y]=False
                print(data)
                x=y
            else:
                break
            
        
for i in range(1,101):
    if data[i]==True:
        print(i)