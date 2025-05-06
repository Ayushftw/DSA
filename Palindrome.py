# Palindrome String 

# def is_palindrome(s):
#     left = 0
#     right = len(s) - 1

#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True

# n = "ANMMNA"
# print(is_palindrome(n))  

# TC -> O(n/2) or 0(n) 
# SC ->O(n)


# Using recusrion 
def is_palindrome(s, left=0, right=None):
    if right is None:
        right = len(s) - 1
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

print(is_palindrome("ANMNMNA")) 
# TC -> O(n/2) or 0(n) 
# SC ->O(n/2) or 0(n) 
