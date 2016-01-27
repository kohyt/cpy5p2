# q12_find_factors.py

# get input
input_integer = input("Please enter a positive integer:")

# verify
while input_integer.isalpha():
    print("Invalid input!")
    input_integer = input("Please enter a positive integer:")
integer = int(input_integer)
while integer < 0:
    print("Invalid input!")
    input_integer = input("Please enter a positive integer:")
    integer = int(input_integer)

# calculation
if integer > 0:
    divisor = 2
    factors = []
    i=0

    while integer != 1:
        divisor = 2
        while integer % divisor != 0:
            divisor += 1
        integer = integer / divisor
        i+=1
        factors.insert(i,divisor)
            
    
print("Factor(s):", factors)
    
    
