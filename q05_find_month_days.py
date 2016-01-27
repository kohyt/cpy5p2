# q05_find_month_days.py

# get input
month = int(input("Enter month:"))
year = int(input("Enter year:"))

if month == 1:
    print("January {0} has 31 days".format(year))
if month == 2:
    if year % 4 == 0:
        print("February {0} has 29 days".format(year))
    elif year % 400 == 0:
        print("February {0} has 29 days".format(year))
    elif year % 100 != 0:
        print("February {0} has 28 days".format(year))
    else:
        print("February {0} has 28 days".format(year))
if month == 3:
    print("March {0} has 31 days".format(year))
if month == 4:
    print("April {0} has 30 days".format(year))
if month == 5:
    print("May {0} has 31 days".format(year))
if month == 6:
    print("June {0} has 30 days".format(year))
if month == 7:
    print("July {0} has 31 days".format(year))
if month == 8:
    print("August {0} has 31 days".format(year))
if month == 9:
    print("September {0} has 30 days".format(year))
if month == 10:
    print("October {0} has 31 days".format(year))
if month == 11:
    print("November {0} has 30 days".format(year))
if month == 12:
    print("December {0} has 31 days".format(year))
while month > 12:
    print("Invalid input!")
    month = int(input("Enter month:"))
    year = int(input("Enter year:"))
while month < 1:
    print("Invalid input!")
    month = int(input("Enter month:"))
    year = int(input("Enter year:"))

