s = "aydnjhidslkfla"
q = ["a", "b", "c", "l", "p"]

hash_list = [0] * 26

for ch in s:
    asci_val = ord(ch)
    index = asci_val - 97
    hash_list[index] += 1

for ch in q:
    asci_val = ord(ch)
    index = asci_val - 97
    print(hash_list[index])

#  TC => o(N+M)
#  SC => 0(1)