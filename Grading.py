while True:
    while True:
        try:
            sub1=float(input("Enter Marks in  General Mathematics:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub2=float(input("Enter Marks in Filipino:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub3=float(input("Enter Marks in  Earth and Life Science:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub4=float(input("Enter Marks in  Physical Education:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub5=float(input("Enter Marks in  Practical Research:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub6=float(input("Enter Marks in  Oral Communication:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub7=float(input("Enter Marks in  Contemporary Philippine Arts from the Regions:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub8=float(input("Enter Marks in  Personal Development:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub9=float(input("Enter Marks in  Philosophy:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub10=float(input("Enter Marks in  Understanding Culture, Politics, and Society:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub11=float(input("Enter Marks in  Applied Economics:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub12=float(input("Enter Marks in  Reading and Writing:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    sum=sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9+sub10+sub11+sub12
    print("The Sum is:", sum)

    percentage=(sum/1200)*100
    print("The percentage is:", percentage)

    #Grading Line
    if percentage>=90:
        print("Excellent work! You got an A+")

    elif percentage>=80:
        print("You're amazing! You got an A")

    elif percentage>=70:
        print("Well done! You got B+")

    elif percentage>=60:
        print("Great job! You got a B")

    elif percentage>=50:
        print("Good effort! You got a C+")

    elif percentage>=40:
        print("Well tried! You got a C")

    elif percentage>=30:
        print("D+")

    else:
        print("You failed. Better luck next time")
    choice = input("Would you like to calculate your grades again? (yes/no): ")
    if choice == "no":
        print("Okay, goodbye! Good luck with your studies!")
        break



