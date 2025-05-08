# Insertion Sort

nums = [3, 5, 6, 1, 23, 2, 5, 8, 10, 4, 1]

n = len(nums)
for i in range(1, n):
    key = nums[i]
    j = i - 1
    while j >= 0 and nums[j] > key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key

print(nums)
# TC -> o(n^2)
# SC -> o(1)