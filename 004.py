def isPalindrome(arg):
    s_arg = str(arg)
    l = int(len(s_arg) / 2)
    a = s_arg[0:l]
    b = s_arg[l:]
    b = b[::-1]
    if a == b:
        return True


num_max = []

for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i * j):
            num_max.append(i * j)

print(max(num_max))