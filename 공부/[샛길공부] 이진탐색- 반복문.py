#반복문을 통한 이진탐색

def binary_search(array,target,start,end):
    while start<=end:
        mid= (start+end)// 2
        #조건1) 중간점이 타켓
        if array[mid]==target:
            return mid
        #조건2) 중간점보다 작음(끝점을 중간점 이전으로 변경)
        elif array[mid]>target:
            end= mid-1
        #조건3) 중간점보다 큼(시작점을 중간점 다음으로 변경)
        else:
            start= mid+1
    return None

n, target = list(map(int,input().split()))
array = list(map(int,input().split()))

#리스트니까 시작점은 0 끝점은 n-1
result=binary_search(array,target,0,n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1) 
    #나열 수 중 몇번째인지 물어보는거니까 인덱스값+1을 해준다
        