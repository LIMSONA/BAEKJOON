# 1부터 10,000까지 들어있는 base data에서 
# 생성자들을 제거하여 셀프넘버를 빼는 원리는 동일

# Keypoint 1
# 생성자가 2개인 아이들이 있기에 여러번 빼려고하면 에러가 생길테니
# 생성자들은 set로 data를 만들어준다.

# Keypoint 2
# 각 자리를 10의 각자리 제곱으로 나눠 주어 도출하기 보다는
# str로 만든 다음 하나씩 도출시키는 방법을 이용

base=set(range(1,10001))
new=set()

for i in range(1,10001):  #1부터 시작하여 생성자data 만들기
    for j in str(i):    #문자열로 바꿔주기
        i += int(j)     #하나씩 나온 str를 int로 바꿔며 더하기
    new.add(i)      #만들어진 생성자를 new data에 추가
    
#셀프넘버 = 기존 - 생성자 / 증가하는 순서로 출력해야하니 정렬    
self= sorted(base - new)

#셀프넘버 하나씩 출력
for i in self:
    print(i)