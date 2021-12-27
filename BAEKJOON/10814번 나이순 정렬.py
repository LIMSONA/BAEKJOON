t=int(input())
join_list=[]

for i in range(t):
    age,name=input().split()
    join_list.append( [int(age),name] ) 
    #age와 name 묶어서 삽입

# age 기준으로 정렬하는데, 그 위치는 lambda로 정의해준다.
# i[0]은 age
join_list.sort( key = lambda i : (i[0]) )


#i[0]은 age, i[1]은 name
for i in join_list:
    print( i[0], i[1] )
