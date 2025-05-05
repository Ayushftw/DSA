# Reverse Array using  Recursion


nums = [5,7,3,2,6,1,5,9]
# num.reverse()
# print(num)
# print(num[::-1])

def Reverse(nums,left,right):
    if left >= right:
        return 
    nums[left], nums[right] = nums[right], nums[left]
    Reverse(nums,left+1,right-1)
Reverse(nums, 0, len(nums) - 1)
print(nums)


#  TC -> O(N)
#  SC ->  O(N)