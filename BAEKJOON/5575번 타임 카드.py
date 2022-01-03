a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))


for i in [a,b,c]:
    st=i[0]*3600 + i[1]*60 + i[2]
    fi=i[3]*3600 + i[4]*60 + i[5]
    
    hrs = fi-st
    
    
    print( hrs//3600 , (hrs%3600)//60 , (hrs%3600)%60 )