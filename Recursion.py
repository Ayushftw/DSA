# Parameterised Recursion

# Print 1 to N using Tail recursion

# def tailRecusrion(i,N):
#     if N == 0:
#         return
#     tailRecusrion(i, N-1)
#     print(N)


# tailRecusrion(1,5)



# Sum of 1 to N

# def sumN(sum,i,N):
#     if i>N:
#         print(sum)
#         return
#     sumN(sum+i,i+1,N)


# sumN(0,1,5)


#  Functional Recursion 


def func(N):
    if N == 1:
        return 1
    return N + func(N - 1)
print(func(4))
