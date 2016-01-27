# q08_top2_scores.py

# get input
number = int(input("Enter number of students:"))

array = [[0 for i in range (number)] for i in range (2)]
for i in range(number):
    array[0][i] = input("Enter student's name:")
    array[1][i] = float(input("Enter student's score:"))

index = array[1].index(max(array[1]))
print("Highest score is", array[1][index])
print("Highest scorer is", array[0][index])
array[1].remove(array[1][index])
array[0].remove(array[0][index])

index = array[1].index(max(array[1]))
print("Second highest score is", array[1][index])
print("Second highest scorer is", array[0][index])






    



