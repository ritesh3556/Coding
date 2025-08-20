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

# Remove duplicate element in O(n)
def removeDuplicates(self, nums: List[int]) -> int:
    ele = nums[0]
    i = 1
    k = 1
    while (i < len(nums)):
        if nums[i] != ele:
            nums[k] = ele = nums[i]

            k += 1
        i += 1
    return k

# rotate array
def reverse(nums, s, e):
    while (s < e):
        nums[s], nums[e] = nums[e], nums[s]
        s += 1
        e -= 1
    return nums


def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n

    reverse(nums, 0, n - k - 1)
    reverse(nums, n - k, n - 1)
    reverse(nums, 0, n - 1)
    return nums


rotate([1, 2, 3, 4, 5])




