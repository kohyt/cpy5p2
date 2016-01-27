# q11_find_gcd.py
# find the greatest GCD

# get input
a = int(input("Enter first integer:"))
b = int(input("Enter second integer:"))


def gcd(a,b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)     

# print result
print ("The Greatest Common Divisor of", a, "and", b, "is", gcd(a,b))






