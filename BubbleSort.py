# Bubble Sort 


nums = [2,3,4,5,9,2,87,2,1,]
n = len(nums)

for i in range (n-2,-1,-1):
    for j in range (0,i+1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]


print(nums)


# TC -> o(n^2)
# SC -> O(1)