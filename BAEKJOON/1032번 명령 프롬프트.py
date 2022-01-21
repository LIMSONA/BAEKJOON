t=int(input())
a=[]
for i in range(t):
    file = input()
    a.append(file)
    
result=''
for i in range(len(a[0])):
    if a[0][i]==a[1][i]==a[2][i]: 
        result=result+(a[0][i])
    else:
        result=result+"?"
        
print(result)