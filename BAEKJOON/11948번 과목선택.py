science=[]
for _ in range(4):
    science.append(int(input()))
    
society=[]
for _ in range(2):
    society.append(int(input()))
    
#4개중 3개의 합 
science= sorted(science,reverse=True)
# 2개중 1개의 합
society= sorted(society,reverse=True)

print(sum(science[0:3])+society[0])
# 위와 동일식
# print(science[0]+science[1]+science[2]+society[0])
