while True:
    while True:
        try:
            sub1=float(input("Enter marks in  General Mathematics:"))
            print(""*10)
            if sub1 < 0 or sub1 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub2=float(input("Enter marks in Filipino:"))
            print(""*10)
            if sub2 < 0 or sub2 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub3=float(input("Enter marks in  Earth and Life Science:"))
            print(""*10)
            if sub3 < 0 or sub3 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub4=float(input("Enter marks in  Physical Education:"))
            print(""*10)
            if sub4 < 0 or sub4 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub5=float(input("Enter marks in  Practical Research:"))
            print(""*10)
            if sub5 < 0 or sub5 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub6=float(input("Enter marks in  Oral Communication:"))
            print(""*10)
            if sub6 < 0 or sub6 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub7=float(input("Enter marks in  Contemporary Philippine Arts from the Regions:"))
            print(""*10)
            if sub7 < 0 or sub7 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub8=float(input("Enter marks in  Personal Development:"))
            print(""*10)
            if sub8 < 0 or sub8 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub9=float(input("Enter marks in  Philosophy:"))
            print(""*10)
            if sub9 < 0 or sub9 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub10=float(input("Enter marks in  Politics:"))
            print(""*10)
            if sub10 < 0 or sub10 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub11=float(input("Enter marks in  Applied Economics:"))
            print(""*10)
            if sub11 < 0 or sub11 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    while True:
        try:
            sub12=float(input("Enter marks in  Reading and Writing:"))
            print(""*10)
            if sub12 < 0 or sub12 > 100:
                print("Only enter a number between 0 - 100")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    total=sub1+sub2+sub3+sub4+sub5+sub6+sub7+sub8+sub9+sub10+sub11+sub12
    print("The Sum is:", total)
    print(""*10)

    percentage=(total/1200)*100
    print(f"The percentage is: {percentage:.2f}")
    print(""*10)

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
        print("You failed. Better luck next time!")
    choice = input("Would you like to calculate your grades again? (yes/no): ").lower()
    if choice == "no":
        print("Okay, goodbye! Good luck with your studies!")
        break