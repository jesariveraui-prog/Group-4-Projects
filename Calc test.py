while True: 
    operator = input("Enter choice (+ - * /): ")

    num1 = float(input("Enter the 1st number: "))
    num2 = float(input("Enter the 2nd number: "))

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
            print("Division by zero is not allowed. Please try again.")
        else: 
            result = num1 / num2
            print(round(result, 3))
    else:
        print(f"{operator} in an invalid operator")

    choice = input("Would you like to continue? (yes/no): ").lower()
    if choice == "no":
        print("Thank you for using this calculator!")
    break