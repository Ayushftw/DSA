nums = [55, -97, 32, 99, 3, 67]

largest = nums[0]

n = len(nums)

for i in range(n):
    largest = max(largest, nums[i])

print(largest)
