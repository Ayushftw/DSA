# Selection Sort 
nums = [5,1,4,8,4,6,9]

def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                  min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

selection_sort(nums)
print(nums)

# TC - O(n^2)
# SC - O(1)  