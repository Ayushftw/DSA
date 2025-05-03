import math 
num = 36
fact = []


# Brute Sol :- (Time Complexicity O(N))

# while n <= num :
#      if num %n == 0:
#       fact.append(n)
#      n +=1
# print(fact)


# for i in range (1, num+1):
#       if num %i == 0:
#        fact.append(i)
# print(fact)


# Better Sol :- iterate till half of the num then append the num  (Time Complexicity O(N/2) almost similar to O(N) removed constant )
# for i in range (1, num//2):
#      if num % i == 0 :
#           fact.append(i)
# fact.append(num)
# print(fact)



# Optimal Sol :- Go till the Sqrt of the num  (Time Complexicity O(Sqrt N) +  O(NlogN) when we sort. If we dont sort the TC will be  O(Sqrt N))


for i in range (1, int(math.sqrt(num))+1):
     if num % i == 0 :
          fact.append(i)
     if num // i != i:
          fact.append(num//i)
fact.sort()  
# sorting here so the TC will include O(NlogN) as TC for sorthing 
print(fact)