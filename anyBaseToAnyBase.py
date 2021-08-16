






def decimal(n,base):
    
    k = 0
    c = 0
    while(n):
        
        c+= base**k * (n%10)
        n//= 10
        k+=1
    
    return c
def base(n,base):
    
    k=0
    c=0
    while(n):
        
        c+= 10**k * (n%base) 
        n//=base
        k+=1
    
    return c    

def anyBaseToAnyBase(n,base1,base2):
    
    d = decimal(n,base1)
    d2 = base(d,base2)
    
    return d2
    
n = int(input())
base1 = int(input())
base2 = int(input())
print(anyBaseToAnyBase(n,base1,base2))

