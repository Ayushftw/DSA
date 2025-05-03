nums = [2,3,4,5,1,3,5,7,3,3,3,2,6,7,8,5,4,3,3]

x = 3
# freq_map = {}
# for i in range(0 , len(nums)):
#     if nums[i] in freq_map:
#       freq_map[nums[i]] +=1
#     else:
#         freq_map[nums[i]] = 1 
# print(freq_map[x])


#  TC -> o(N)
#  SC -> o(N)

n=len(nums)
hash_map = {}
for i in range(0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)

# TC -> O(N)  Avg case - o(1)