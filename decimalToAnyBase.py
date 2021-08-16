

def divideByBase(n,base):
    
    k = 0
    c = 0
    while(n):
        
        c+=10**k * (n%base)
        n//=base
        k+=1
    
    return c

n = int(input())
base = int(input())
print(divideByBase(n,base))