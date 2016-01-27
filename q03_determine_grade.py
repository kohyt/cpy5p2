# q03_determine_grade.py

# get input
input_score = input("Enter score:")

while input_score.isalpha():
    print("Invalid input!")
    input_score = input("Enter score:")

if input_score.isnumeric():
    score = float(input_score)
    if score >= 70 and score <= 100:
        print("A")
    elif score >= 60 and score <= 69:
        print("B")
    elif score >= 55 and score <= 59:
        print("C")
    elif score >= 50 and score <= 54:
        print("D")
    elif score >= 45 and score <= 49:
        print("E")
    elif score >= 35 and score <= 44:
        print("S")
    elif score >= 0 and score <= 35:
        print("U")
    else:
        print("Invalid! Score must be within 0 - 100")
        input_score = input("Enter score:")
        score = float(input_score)
        if score >= 70 and score <= 100:
            print("A")
        elif score >= 60 and score <= 69:
            print("B")
        elif score >= 55 and score <= 59:
            print("C")
        elif score >= 50 and score <= 54:
            print("D")
        elif score >= 45 and score <= 49:
            print("E")
        elif score >= 35 and score <= 44:
            print("S")
        elif score >= 0 and score <= 35:
                print("U")
            


                    





