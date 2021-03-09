nums = [[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]
def funct(nums):
    for a in nums:
        for j in range(len(a)//2):
            a[j], a[-j-1]=a[-j-1], a[j]
    return nums
print(funct(nums))
