# # m줄의 수가 N줄에 들어있는가?
# # m이 들어있으면 1 true 없으면 0 false

# # 1차시도 실패 -------------
n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

for i in m_list:
    if i in n_list:
        print(1)
    else:
        print(0)

#2차시도(성공) -------------------------
#재귀함수 이용---------------------
n=int(input())
n_list=list(map(int,input().split()))
n_list.sort( )

m=int(input())
m_list=list(map(int,input().split()))

def binary(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2
    #조건1) 중간점이 타켓
    if target == array[mid]:
        return 1
    #조건2) 중간점보다 작음(끝점을 중간점 이전으로 변경)
    elif target < array[mid]:
        return binary(array, target, start, mid-1)
    #조건3) 중간점보다 큼(시작점을 중간점 다음으로 변경)
    else:
        return binary(array, target, mid+1, end)

for target in m_list:   #타겟을 반복문으로 돌리고
    start = 0
    end = len(n_list)-1
    print(binary(n_list, target, start, end))
    
#반복문 사용-------------------------------------------    
    
n=int(input())
n_list=list(map(int,input().split()))
n_list.sort( )

m=int(input())
m_list=list(map(int,input().split()))

def binary(array,target,start,end):
    while start<=end:
        mid= (start+end)// 2
        
        #조건1) 중간점이 타켓
        if array[mid]==target:
            return 1    #있을 때
        
        #조건2) 중간점보다 작음(끝점을 중간점 이전으로 변경)
        elif array[mid]>target:
            end= mid-1
        
        #조건3) 중간점보다 큼(시작점을 중간점 다음으로 변경)
        else:
            start= mid+1
    return 0    #없을 때


for target in m_list:   #타겟을 반복문으로 돌리고
    start = 0
    end = len(n_list)-1
    print(binary(n_list, target, start, end))