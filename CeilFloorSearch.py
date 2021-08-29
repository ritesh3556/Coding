def bs(l,item):
    
    lo = 0
    hi = len(l)-1
    ceil = 1000000001
    floor = -1000000001
    while(lo<=hi):
        
        mid = (lo+hi)//2
        
        if l[mid]==item:
            return mid
        
        
        elif l[mid]< item:
            lo = mid+1
            floor=l[mid]
        else:
            hi = mid -1
            ceil=l[mid]
    
    print(ceil)
    print(floor)

    
        
l = [int(input()) for i in range(int(input()))]
bs(l,int(input()))