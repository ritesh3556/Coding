



def anyBaseAdd(base,n1,n2):
    
    
    s=""
    c=0
    while(n1 or n2 or c):
        
        a = (n1%10)+(n2%10)+c
        s = str(a%base)+s
        c = a//base
        
        n1//=10
        n2//=10
        
    return s    
base=int(input())
n1=int(input())
n2=int(input())
print(anyBaseAdd(base,n1,n2))
