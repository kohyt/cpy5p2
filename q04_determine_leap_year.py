# q04_determine_leap_year.py

# get input
input_year = input("Enter year:")
while input_year.isalpha():
    print("Invalid input!")
    input_year = input("Enter year:")
year = int(input_year)
if year % 4 == 0:
    print("Leap")
elif year % 400 == 0:
    print("Leap")
elif year % 100 != 0:
    print("Non-leap")
else:
    print("Non-leap")
