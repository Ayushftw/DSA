# Factorial Using recursion 



def fact(n):
   if n <= 1 :
    return 1
   return n* fact((n-1))

print(fact(4))  


# TC -> O(N)
# SC -> O(N) due to recursive call stack