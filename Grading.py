while True:
    while True:
        try:
            n1=float(input("Enter Marks in  General Mathematics:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n2=float(input("Enter Marks in Filipino:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n3=float(input("Enter Marks in  Earth and Life Science:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n4=float(input("Enter Marks in  Physical Education:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n5=float(input("Enter Marks in  Practical Research:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n6=float(input("Enter Marks in  Oral Communication:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n7=float(input("Enter Marks in  Contemporary Philippine Arts from the Regions:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n8=float(input("Enter Marks in  Personal Development:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n9=float(input("Enter Marks in  Philosophy:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n10=float(input("Enter Marks in  Understanding Culture, Politics, and Society:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n11=float(input("Enter Marks in  Applied Economics:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            n12=float(input("Enter Marks in  Reading and Writing:"))
            break
        except ValueError:
            print("Please enter a valid number.")
    sum=n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11+n12
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


