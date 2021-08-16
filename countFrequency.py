


def countFrequency(arr,item):

    count=0

    for i in arr:
        if i==item:
            count+=1

    return count

n = int(input())
l = list(map(int,input().split()))
item = int(input())
print(countFrequency(l,item))



