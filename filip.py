a,b=map(int,input().split()) 

reva=int(str(a)[::-1]) 
revb=int(str(b)[::-1]) 

if reva>revb: 
    print(reva) 
else: 
    print(revb)

