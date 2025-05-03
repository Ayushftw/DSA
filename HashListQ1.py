n = [2,1,4,5,5,5,6,6,7,7,3,2,3,3,2,9,2]
m = [5,4,3,2,6,7,10]


#  Brute force   TC -> O(N*M), SC O(1)
for i in m:
    count = 0 
    for x in n:
        if x == i:
            count +=1
    print(count)    




#  Optimal force   TC -> O(N+M), SC O(1)

# hash_list = [0] * 11

# for nums in n:
#     hash_list[nums] += 1 

# for num in m:
#     if num< 1 or num > 10:
#         print (0) 
#     else:
#         print(hash_list[num])