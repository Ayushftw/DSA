# Armstrong Number

num = 123
n = num
nod = len(str(num))
result = 0
while n > 0:
    digit = n%10
    result += digit**nod
    n = n//10
print(result == num)

