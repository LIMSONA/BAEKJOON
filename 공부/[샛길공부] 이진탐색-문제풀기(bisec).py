n,x = map(int, input().split())
array=list(map(int, input().split()))

from bisect import bisect_left, bisect_right

def count(array, left_v, right_v):
    left_ind = bisect_left(array, left_v)
    right_ind = bisect_right(array, right_v)
    return right_ind - left_ind

#결과값
result = count(array,x,x)

#없으면 -1출력
if result == 0:
    print(-1)
#있으면 갯수 출력
else:
    print(result)