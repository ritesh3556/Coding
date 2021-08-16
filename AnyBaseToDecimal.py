



def divideByBase(n,base):
    
    k = 0
    c = 0
    while(n):
        
        c+= base**k * (n%10)
        n//= 10
        k+=1
    
    return c

n = int(input())
base = int(input())
print(divideByBase(n,base))