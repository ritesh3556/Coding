#Second largest element

def sle():
    a = list(map(int, input().split()))
    i = 0
    maxx1 = -10**10
    maxx2 = -10**10
    while(i<len(a)):
        if a[i] > maxx1:
            maxx2 = maxx1
            maxx1 = a[i]
        elif a[i] > maxx2 and a[i]!=maxx1:
            maxx2 = a[i]

        i+=1

    if maxx2!=-10**10:
        print(maxx2)
    else:
        print("no second largest element available")

sle()