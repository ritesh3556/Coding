

l = [int(input()) for i in range(int(input()))]

k=int(input())%len(l)


start=len(l)-k
end= len(l)-1

while(start<=end):
    
    temp = l[start]
    l[start]=l[end]
    l[end]=temp
    start+=1
    end-=1
start=0
end=len(l)-k-1

while(start<end):
    
    temp = l[start]
    l[start]=l[end]
    l[end]=temp
    start+=1
    end-=1
start=0
end=len(l)-1

while(start<=end):
    
    temp = l[start]
    l[start]=l[end]
    l[end]=temp
    start+=1
    end-=1

for i in l:
    print(i,end=' ')
    

    
    
    
    