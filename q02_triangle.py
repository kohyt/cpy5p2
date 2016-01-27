# q02_triangle.py

##a = int(input("Enter side 1:"))
##b = int(input("Enter side 2:"))
##c = int(input("Enter side 3:"))
##
##def check_input():
##    if a + b > c and b + c > a and c + a > b:
##        return True
##    else:
##        return False
##    
##if check_input():
##    perimeter = a + b + c
##    print("Perimeter =", perimeter)
##    
##else:
##    print("Invalid triangle!")

side_1 = input("Enter side 1:")
side_2 = input("Enter side 2:")
side_3 = input("Enter side 3:")
while side_1.isalpha() and side_2.isalpha() and side_3.isalpha():
    print("Invalid input!")
    side_1 = input("Enter side 1:")
    side_2 = input("Enter side 2:")
    side_3 = input("Enter side 3:")
side_1 = float(side_1)
side_2 = float(side_2)
side_3 = float(side_3)
a = [side_1, side_2, side_3]
a.sort()
if side_1 + side_2 > side_3:
    perimeter = side_1 + side_2 + side_3
    print("Perimeter=", perimeter)
else:
    print("Invalid triangle!")

