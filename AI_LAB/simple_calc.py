while True:
    # Display the menu
    print("\nSimple Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    # Take the user's choice
    choice = int(input("\nEnter your choice (1-5): "))

    if choice in [1, 2, 3, 4]:
        # Take two numbers as input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform the appropriate operation
        if choice == 1:
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == 2:
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == 3:
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")

    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
