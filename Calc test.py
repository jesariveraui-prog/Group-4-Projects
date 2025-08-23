while True: 
    operator = input("Enter an operator (+ - * /): ")
    while True:
        try:
            num1 = float(input("Enter your 1st number: "))
            break
        except ValueError:
            print("That is not a valid number." )
    while True:
        try:
            num2 = float(input("Enter your 2nd number: "))
            break
        except ValueError:
            print("That is not a valid number." )
    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
    elif operator == "/":
        if num2 == 0:
            print("Division by zero is not allowed. Please try another number.")
        else: 
            result = num1 / num2
            print(round(result, 3))
    else:
        print(f"{operator} is an invalid operator")

    choice = input("Would you like to try it again? (yes/no): ").lower()
    if choice == "no":
        print("Thank you for using this calculator!♡")
    break

