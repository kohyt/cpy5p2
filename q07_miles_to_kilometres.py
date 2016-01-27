# q07_miles_to_kilometres.py

print("Miles Kilometres   Kilometres Miles") 
for x in range (1,11):
    i = (x + 3) * 5
    print("{0:<5}".format(x), "{0:<8.3f}".format(x*1.609), "{0:>6}".format(i), "{0:>14.3f}".format(i/1.609))


