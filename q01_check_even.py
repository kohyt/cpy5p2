# q01_check_even.py

# get input
##number = input("Enter number:")
##
### check validity then even or odd
##if number.isnumeric():
##    input_number = int(number)
##    if input_number % 2 == 1:
##        print("{0} is odd".format(number))
##    else:
##        print("{0} is even".format(number))
##
##else:
##    print("Invalid input!"):
##    number = input("Enter number:")
##    if number.isnumeric():
##        input_number = int(number)
##        if input_number % 2 == 1:
##            print("{0} is odd".format(number))
##        else:
##            print("{0} is even".format(number))
##    else:
##        print("Invalid input!")

boolean = True
while boolean:
    number = input("Enter number:")
    if number.isnumeric():
        input_number = int(number)
        if input_number % 2 == 1:
            print("{0} is odd".format(number))
        else:
            print("{0} is even".format(number))
    else:
        print("Invalid input!")
        
            


        
