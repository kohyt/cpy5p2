# q10_find_largest.py
#  find largest integer n such that n3 < 12000

n = 0
while n ** 3 < 12000:
    n += 1

# result
print(n - 1)


