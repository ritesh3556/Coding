
#anybaseSub



def anyBaseSub(base, n1,n2):
    
    
    r=0
    p=1
    c=0
    while(n1 or n2 or c):
        
        
        d1 = (n1%10)
        d2 = (n2%10)
        n1//=10
        n2//=10
        
        d2 = d2+c
        if d2>=d1:
            
            c=0
            d = d2-d1
        else:
            c=-1
            d = d2+base-d1
        
        r += d*p
        p*=10
    
    return r

base = int(input())
n1 = int(input())
n2 = int(input())
print(anyBaseSub(base,n1,n2))
