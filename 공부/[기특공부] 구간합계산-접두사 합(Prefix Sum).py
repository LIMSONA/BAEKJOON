#왼쪽(시작점), 오른쪽(끝점)
left, right = map(int,input().split()) 

n = int(input())    #데이터 개수
data = list(map(int,input().split()))   #데이터 열

sum_value = 0
# [1]부터 append해야하니 [0]자리에 미리 0을 삽입하는 리스트
prefix_sum = [0]        

#합계값 리스트에 넣는 반복문
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)
    
print(prefix_sum[right] - prefix_sum[left-1])